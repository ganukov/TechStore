from ProjectDefence.products.forms import ProductForm
from ProjectDefence.products.models import Product
from django.contrib import admin


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'make', 'choice', 'price')
    form = ProductForm
