from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products.views import ProductViewSet, CategoryViewSet
from convertor.views import CurrencyListCreateView, CurrencyRetrieveUpdateDestroyView

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'currencies', CurrencyListCreateView)

urlpatterns = [
    path('', include(router.urls)),
]
