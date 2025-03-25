from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.filters import SearchFilter
from django_filters. rest_framework import DjangoFilterBackend
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] 
    filter_backends = [SearchFilter, SearchFilter]
    search_fields = ['name', 'description']
    filterset_fields = ['category', 'brand', 'price']
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            self.permission_classes = [IsAdminUser]  
        return super().get_permissions()
