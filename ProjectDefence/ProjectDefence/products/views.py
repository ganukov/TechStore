from ProjectDefence.cart.models import Order, OrderItem
from ProjectDefence.products.forms import ProductForm
from ProjectDefence.products.models import Product
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views


def add_product(request):
    form = ProductForm()
    items_in_cart = sum([item.quantity for item in OrderItem.objects.all()])

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

        context = {'form': form, 'items_in_cart': items_in_cart, }
        return render(request, 'products/add_product.html', context)

    context = {'form': form, 'items_in_cart': items_in_cart, }
    return render(request, 'products/add_product.html', context)


# class ProductAddView(views.FormView):
#     template_name = 'products/add_product.html'
#     form_class = ProductForm
#     success_url = reverse_lazy('home')

class DetailsProductView(views.DetailView):
    template_name = 'products/details_product.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super(DetailsProductView, self).get_context_data(**kwargs)
        if Order.objects.all() != 0:
            context['items_in_cart'] = sum([item.quantity for item in OrderItem.objects.all()])
        else:
            context['items_in_cart'] = 0
        return context


class LaptopsListView(views.ListView):
    template_name = 'products/laptops.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super(LaptopsListView, self).get_context_data(**kwargs)
        context['laptops'] = Product.objects.filter(choice='Laptop')

        if Order.objects.all() != 0:
            context['items_in_cart'] = sum([item.quantity for item in OrderItem.objects.all()])
        else:
            context['items_in_cart'] = 0
        return context


class PhonesListView(views.ListView):
    template_name = 'products/phones.html'
    model = Product
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super(PhonesListView, self).get_context_data(**kwargs)
        context['phones'] = Product.objects.filter(choice='Phone')

        if Order.objects.all() != 0:
            context['items_in_cart'] = sum([item.quantity for item in OrderItem.objects.all()])
        else:
            context['items_in_cart'] = 0
        return context


class ConsolesListView(views.ListView):
    template_name = 'products/consoles.html'
    model = Product
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super(ConsolesListView, self).get_context_data(**kwargs)
        context['consoles'] = Product.objects.filter(choice='Console')

        if Order.objects.all() != 0:
            context['items_in_cart'] = sum([item.quantity for item in OrderItem.objects.all()])
        else:
            context['items_in_cart'] = 0
        return context


class AllProductsView(views.ListView):
    template_name = 'products/all_products.html'
    model = Product
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super(AllProductsView, self).get_context_data(**kwargs)
        context['products'] = Product.objects.all()

        if Order.objects.all() != 0:
            context['items_in_cart'] = sum([item.quantity for item in OrderItem.objects.all()])
        else:
            context['items_in_cart'] = 0
        return context
