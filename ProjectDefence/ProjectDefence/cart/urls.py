from ProjectDefence.cart.views import checkout, update_item, CartApiView, cart
from django.urls import path

urlpatterns = (
    path('', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('update-item/', update_item, name='update item'),
    path('orders/', CartApiView.as_view(), name='api get order details'),
)
