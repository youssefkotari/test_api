# urls.py
from django.urls import path, include
from rest_framework import routers
from .views import CategoryViewSet, ProductViewSet, ProductImageViewSet

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'product-images', ProductImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]