from django.contrib import admin
from .models import InventoryItem, Category, InventoryChange

# Register models
admin.site.register(Category)
admin.site.register(InventoryChange)

@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'quantity', 'price', 'category', 'date_added', 'last_updated')
    list_filter = ('category',)
    search_fields = ('name', 'description', 'owner__username')
