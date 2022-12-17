import json

from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ProjectDefence.accounts.forms import ProfileCheckForm, ProfileFullfilForm
from ProjectDefence.accounts.models import AppUser
from ProjectDefence.cart.models import Order, OrderItem
from ProjectDefence.products.models import Product
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework import generics as rest_views
from rest_framework import serializers
from rest_framework import viewsets

UserModel = get_user_model()


# cart/orders/
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = OrderItem
        fields = '__all__'


class CartApiView(rest_views.ListAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.profile
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all().order_by('pk')
        cart_items = order.cart_items
        items_in_cart = cart_items
    else:
        return redirect('sign up')

    context = {'items': items, 'order': order, 'cart_items': cart_items, 'items_in_cart': items_in_cart, }
    return render(request, 'common/../../templates/cart/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.profile
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all().order_by('pk')
        form = ProfileFullfilForm(initial=customer.__dict__)
        items_in_cart = order.cart_items

        if request.method == 'POST':
            form = ProfileFullfilForm(request.POST, instance=customer)

            if form.is_valid():
                form.save()
                order.delete()
                items.delete()
                OrderItem.objects.all().delete()
                context = {'customer': customer, 'items_in_cart': items_in_cart, }
                return render(request, 'common/../../templates/cart/placed_order.html', context)

            context = {'items': items, 'order': order, 'form': form, 'items_in_cart': items_in_cart, }
            return render(request, 'common/../../templates/cart/checkout.html', context)

        context = {'items': items, 'order': order, 'form': form, 'items_in_cart': items_in_cart, }
        return render(request, 'common/../../templates/cart/checkout.html', context)

    else:
        return redirect('sign up')


def update_item(request):
    data = json.loads(request.body)
    product_id = data['product_id']
    action = data['action']

    customer = request.user.profile
    product = Product.objects.get(id=product_id)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    order_item, created = OrderItem.objects.get_or_create(order=order, product=product)
    if action == 'add':
        order_item.quantity += 1
    elif action == 'remove':
        order_item.quantity -= 1
    order_item.save()

    if order_item.quantity <= 0:
        order_item.delete()
    return JsonResponse('Item was added', safe=False)

# class OrderUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserModel
#         fields = ("id", "email", "date_joined")
#
#
# class CartSerializer(serializers.ModelSerializer):
#     user = OrderUserSerializer(read_only=True)
#
#     class Meta:
#         model = OrderItem
#
#
# class CartUpdateViewSet(viewsets.ModelViewSet):
#     serializer_class = CartSerializer
#     permission_classes = (IsAuthenticated,)
#     queryset = OrderItem.objects.all()
#
#     def post(self, request):
#         product = Product.objects.get(id=request.body['product_id'])
#         order, created = Order.objects.get_or_create(customer=request.user.profile, complete=False)
#         order_item, created = OrderItem.objects.get_or_create(order=order, product=product)
#         if request.body['action'] == 'add':
#             order_item.quantity += 1
#         elif request.body['action'] == 'remove':
#             order_item.quantity -= 1
#         order_item.save()
#
#         if order_item.quantity <= 0:
#             order_item.delete()
#
#         return Response(status=201)
#
