from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.name

class InventoryItem(models.Model):
    owner = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    category = models.ForeignKey(Category, related_name='items', on_delete=models.SET_NULL, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class InventoryChange(models.Model):
    RESTOCK = 'RESTOCK'
    SALE = 'SALE'
    ADJUSTMENT = 'ADJUSTMENT'
    CHANGE_TYPES = [
        (RESTOCK, 'Restock'),
        (SALE, 'Sale'),
        (ADJUSTMENT, 'Adjustment')
    ]
    item = models.ForeignKey(InventoryItem, related_name='changes', on_delete=models.CASCADE)
    changed_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    change_type = models.CharField(max_length=20, choices=CHANGE_TYPES)
    quantity_before = models.IntegerField()
    quantity_after = models.IntegerField()
    change = models.IntegerField()
    note = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
