from ProjectDefence.cart.views import cart, checkout, update_item
from django.urls import path

urlpatterns = (
    path('', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('update-item/',update_item,name='update item'),
)
