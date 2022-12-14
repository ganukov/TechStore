from ProjectDefence.accounts.forms import SignUpForm, SignInForm
from django.shortcuts import render
from django.contrib.auth import views as auth_views, get_user_model, login
from django.urls import reverse_lazy
from django.views import generic as views

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
