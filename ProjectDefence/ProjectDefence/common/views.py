from django.shortcuts import render

from ProjectDefence.cart.models import OrderItem, Order
from ProjectDefence.common.forms import ContactForm
from ProjectDefence.products.models import Product
from django.contrib.auth import get_user_model
from django.views import generic as views

UserModel = get_user_model()


class HomePageView(views.ListView):
    template_name = 'common/index.html'
    model = Product
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        context['items_in_cart'] = sum([item.quantity for item in OrderItem.objects.all()])
        return context


class AboutPageView(views.TemplateView):
    template_name = 'common/about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutPageView, self).get_context_data(**kwargs)

        if Order.objects.all() != 0:
            context['items_in_cart'] = sum([item.quantity for item in OrderItem.objects.all()])
        else:
            context['items_in_cart'] = 0
        return context


class ContactUsPageView(views.TemplateView):
    template_name = 'common/contact.html'

    def get_context_data(self, **kwargs):
        context = super(ContactUsPageView, self).get_context_data(**kwargs)

        if Order.objects.all() != 0:
            context['items_in_cart'] = sum([item.quantity for item in OrderItem.objects.all()])
        else:
            context['items_in_cart'] = 0
        return context


def complaint_form(request):
    form = ContactForm
    user = request.user
    items_in_cart = sum([item.quantity for item in OrderItem.objects.all()])

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            items_in_cart = sum([item.quantity for item in OrderItem.objects.all()])
            return render(request, 'common/submitted_enquiry.html', context={'items_in_cart': items_in_cart})

        context = {'form': form, 'user': user, 'items_in_cart': items_in_cart}
        return render(request, 'common/contact_us_form.html', context)

    context = {'form': form, 'user': user, 'items_in_cart': items_in_cart}
    return render(request, 'common/contact_us_form.html', context)

    # def get_context_data(self, **kwargs):
    #     context = super(ContactUsFormView, self).get_context_data(**kwargs)
    #     if Order.objects.all() != 0:
    #         context['items_in_cart'] = sum([item.quantity for item in OrderItem.objects.all()])
    #     else:
    #         context['items_in_cart'] = 0
    #     return context
