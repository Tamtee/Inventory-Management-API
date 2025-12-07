from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InventoryItemViewSet, UserViewSet, CategoryViewSet

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('categories', CategoryViewSet)
router.register('items', InventoryItemViewSet, basename='items')

urlpatterns = [
    path('', include(router.urls)),
]
