from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from app_cinema.forms import UserCreateForm


class UserRegisterView(CreateView):
    template_name = 'register.html'
    form_class = UserCreateForm
    success_url = '/'


class UserLoginView(LoginView):
    # https://ccbv.co.uk/projects/Django/4.1/django.contrib.auth.views/LoginView/
    success_url = reverse_lazy('index')
    template_name = 'login.html'
    
    def get_success_url(self):
        return self.success_url


class UserLogoutView(LoginRequiredMixin, LogoutView):
    next_page = '/'
    login_url = 'login/'