from django.shortcuts import render,get_object_or_404
from .serializers import ReviewSerializer
from .models import  Review
from rest_framework import viewsets,status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from product.models import Product
from rest_framework.response import Response

# Create your views here.


class ReviewSet(viewsets.ModelViewSet):
    
    
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Review.objects.filter(product_id =self.kwargs["product_id"])
    
    def create(self,request,product_id):
        
        product = get_object_or_404(Product,id=product_id)
        
        if Review.objects.filter(product=product,user = request.user).exists():
            return Response({"error": "You already reviewed this product."}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save(product=product, user = request.data)
            return Response(serializer.data,status=status.HTTP_200_OK)

        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,product_id,pk=None):
        
        review = get_object_or_404(Review,product_id=product_id,user = request.user)

        serializer = self.get_serializer(review,data=request.data,partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    
    
    def delete(self,request,product_id,pk=None):
        
        review = get_object_or_404(Review,id=pk,product_id=product_id,user=request.user)

        review.delete()

        return Response({'message': "Review deleted"},status=status.HTTP_204_NO_CONTENT)
        

            