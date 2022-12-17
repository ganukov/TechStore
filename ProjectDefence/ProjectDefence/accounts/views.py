from ProjectDefence.accounts.forms import SignUpForm, SignInForm
from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views, get_user_model, login
from django.urls import reverse_lazy
from django.views import generic as views
from ProjectDefence.accounts.forms import ProfileFullfilForm, ProfileCheckForm, ProfileDeleteForm
from ProjectDefence.accounts.models import Profile, AppUser
from ProjectDefence.cart.models import Order, OrderItem

UserModel = get_user_model()


class SignUpView(views.CreateView):
    template_name = 'accounts/sign_up.html'
    form_class = SignUpForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class SignInView(auth_views.LoginView):
    template_name = 'accounts/sign_in.html'
    success_url = reverse_lazy('home')


class SignOutView(auth_views.LogoutView):
    next_page = reverse_lazy('home')


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
    if request.user.is_authenticated:
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
    return redirect('sign up')
