from urllib import request

from ProjectDefence.accounts.forms import ProfileFullfilForm, ProfileCheckForm, ProfileDeleteForm
from ProjectDefence.accounts.models import Profile, AppUser
from ProjectDefence.cart.models import Order, OrderItem
from ProjectDefence.common.forms import ContactForm
from ProjectDefence.products.models import Product
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
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


class ProfileDetailsView(views.DetailView):
    template_name = 'common/../../templates/accounts/profile.html'
    model = UserModel
    form_class = ProfileCheckForm

    def get_context_data(self, **kwargs):
        context = super(ProfileDetailsView, self).get_context_data(**kwargs)
        if Order.objects.all() != 0:
            context['items_in_cart'] = sum([item.quantity for item in OrderItem.objects.all()])
        else:
            context['items_in_cart'] = 0
        return context


class ProfileDeleteView(views.DeleteView):
    template_name = 'common/../../templates/accounts/delete_profile.html'
    model = UserModel
    form_class = ProfileDeleteForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super(ProfileDeleteView, self).get_context_data(**kwargs)
        if Order.objects.all() != 0:
            context['items_in_cart'] = sum([item.quantity for item in OrderItem.objects.all()])
        else:
            context['items_in_cart'] = 0
        return context


def profile_update(request, pk):
    profile = Profile.objects.get(pk=pk)
    form = ProfileFullfilForm(initial=profile.__dict__)
    items_in_cart = sum([item.quantity for item in OrderItem.objects.all()])
    if request.method == 'POST':
        form = ProfileFullfilForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details', pk=pk)
        context = {
            'form': form,
            'profile': profile,
            'items_in_cart': items_in_cart,
        }
        return render(request, 'common/../../templates/accounts/update_profile.html', context)
    context = {
        'form': form,
        'profile': profile,
        'items_in_cart': items_in_cart,

    }
    return render(request, 'common/../../templates/accounts/update_profile.html', context)


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


class ContactUsFormView(views.FormView):
    template_name = 'common/contact_us_form.html'
    form_class = ContactForm

    def get_context_data(self, **kwargs):
        context = super(ContactUsFormView, self).get_context_data(**kwargs)
        if Order.objects.all() != 0:
            context['items_in_cart'] = sum([item.quantity for item in OrderItem.objects.all()])
        else:
            context['items_in_cart'] = 0
        return context
