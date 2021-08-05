from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect

from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView

from .forms import NewUserForm
from django.contrib.auth import logout
from django.contrib import messages


class RegisterView(CreateView):
    model = User
    form_class = NewUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('home')


class SignInView(LoginView):

    template_name = '/registration/login.html'
    success_url = reverse_lazy('home')
