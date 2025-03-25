from django.urls import path,include
from .views import ReviewSet
from rest_framework import routers
from rest_framework.routers import DefaultRouter


router =DefaultRouter()

router.register('product/(?P<product_id>\d+)',ReviewSet,basename='product-review')

urlpatterns = [
    path('', include(router.urls))
]




