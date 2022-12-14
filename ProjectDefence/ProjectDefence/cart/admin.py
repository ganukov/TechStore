from ProjectDefence.cart.models import Order, OrderItem
from django.contrib import admin


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    pass


