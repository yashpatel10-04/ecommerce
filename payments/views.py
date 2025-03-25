from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.shortcuts import get_object_or_404
from .models import Payment
from .serializers import PaymentSerializer
import uuid

class PaymentViewSet(viewsets.ViewSet):
    """Handles payment-related operations."""

    permission_classes = [IsAuthenticated]

    def create(self, request):
        """Initiate a new payment."""
        order_id = str(uuid.uuid4())  
        data = {
            "user": request.user.id,
            "order_id": order_id,
            "amount": request.data.get("amount"),
            "status": "pending",
        }
        serializer = PaymentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Payment initiated!", "payment": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Verify payment by order ID."""
        payment = get_object_or_404(Payment, order_id=pk)
        serializer = PaymentSerializer(payment)
        return Response(serializer.data)

    def update(self, request, pk=None):
        """Update payment status (Used for verifying payments)."""
        payment = get_object_or_404(Payment, order_id=pk)
        serializer = PaymentSerializer(payment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Payment status updated!", "payment": serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """Refund a payment (Admin Only)."""
        if not request.user.is_staff:
            return Response({"error": "Only admins can process refunds."}, status=status.HTTP_403_FORBIDDEN)
        
        payment = get_object_or_404(Payment, order_id=pk)
        if payment.status != "successful":
            return Response({"error": "Only successful payments can be refunded."}, status=status.HTTP_400_BAD_REQUEST)

        payment.status = "refunded"
        payment.save()
        return Response({"message": "Payment refunded successfully!"}, status=status.HTTP_200_OK)
