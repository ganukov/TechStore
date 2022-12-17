from ProjectDefence.cart.models import Order, OrderItem
from django.contrib import admin


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    ordering = ('pk', 'customer', 'date_ordered', 'complete', 'transaction_id',)
    list_display = ['pk', 'customer', 'date_ordered', 'complete', 'transaction_id', 'cart_total', 'cart_items']
    list_filter = ('transaction_id', 'customer', 'date_ordered')
    search_fields = ('complete', 'transaction_id', 'pk')
    sortable_by = ('pk', 'customer', 'date_ordered',)


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    ordering = ('pk', 'product', 'order', 'quantity', 'date_added',)
    list_display = ['pk', 'product', 'order', 'quantity', 'date_added', 'total']
    list_filter = ('product', 'order', 'date_added',)
    search_fields = ('date_added', 'pk')
    sortable_by = ('product', 'order','date_added',)
