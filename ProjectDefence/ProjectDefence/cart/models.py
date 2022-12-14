from ProjectDefence.accounts.models import Profile
from ProjectDefence.products.models import Product
from django.db import models


class Order(models.Model):
    customer = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def cart_total(self):
        return sum([item.total for item in self.orderitem_set.all()])

    @property
    def cart_items(self):
        return sum([item.quantity for item in self.orderitem_set.all()])


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def total(self):
        return self.quantity * self.product.price


