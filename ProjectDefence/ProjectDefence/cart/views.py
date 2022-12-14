import json
from ProjectDefence.accounts.forms import ProfileCheckForm, ProfileFullfilForm
from ProjectDefence.accounts.models import AppUser
from ProjectDefence.cart.models import Order, OrderItem
from ProjectDefence.products.models import Product
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.http import JsonResponse

UserModel = get_user_model()


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
    print('Action', action)
    print('ProductId', product_id)

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
