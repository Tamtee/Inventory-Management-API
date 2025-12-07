from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import InventoryItem, InventoryChange, Category
from .serializers import InventoryItemSerializer, InventoryChangeSerializer, UserSerializer, CategorySerializer
from .permissions import IsOwnerOrReadOnly

# User ViewSet
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]  # Only admin can manage users

# Category ViewSet
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

# Inventory Item ViewSet
class InventoryItemViewSet(viewsets.ModelViewSet):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'quantity', 'price', 'date_added']

    # Assign owner automatically on creation
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    # View inventory change history
    @action(detail=True, methods=['get'])
    def history(self, request, pk=None):
        item = self.get_object()
        changes = item.changes.all()
        serializer = InventoryChangeSerializer(changes, many=True)
        return Response(serializer.data)
