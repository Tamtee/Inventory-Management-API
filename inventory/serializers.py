from rest_framework import serializers
from django.contrib.auth.models import User
from .models import InventoryItem, InventoryChange, Category

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
    
    def create(self, validated_data):
        user = User(username=validated_data['username'], email=validated_data.get('email'))
        user.set_password(validated_data['password'])
        user.save()
        return user

# Category Serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

# Inventory Item Serializer
class InventoryItemSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',
        write_only=True,
        required=False,
        allow_null=True
    )

    class Meta:
        model = InventoryItem
        fields = ['id', 'owner', 'name', 'description', 'quantity', 'price', 'category', 'category_id', 'date_added', 'last_updated']

# Inventory Change Serializer
class InventoryChangeSerializer(serializers.ModelSerializer):
    changed_by = serializers.ReadOnlyField(source='changed_by.username')
    item = serializers.ReadOnlyField(source='item.id')

    class Meta:
        model = InventoryChange
        fields = ['id', 'item', 'changed_by', 'change_type', 'quantity_before', 'quantity_after', 'change', 'note', 'created_at']
