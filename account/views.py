from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.forms import forms
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

#
# def register_request(request):
#     if request.method == "POST":
#         form = NewUserForm(request.POST)
#
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             messages.success(request, "Registration successful.")
#             return redirect("home")
#         messages.error(request, "Unsuccessful registration. Invalid information.")
#     form = NewUserForm()
#     return render(request=request, template_name="register.html", context={"register_form": form})



class RegisterView(CreateView):
    model = User
    form_class = NewUserForm
    template_name = 'account/register.html'
    success_url = reverse_lazy('home')


class SignInView(LoginView):
    template_name = 'account/login.html'
    success_url = reverse_lazy('home')



# def login_request(request):
#     if request.method == "POST":
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 messages.info(request, f"You are now logged in as {username}.")
#                 return redirect("home")
#             else:
#                 messages.error(request, "Invalid username or password.")
#
#         else:
#             messages.error(request,"Invalid username or password.")
#
#     form = AuthenticationForm()
#     return render(request=request, template_name="login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("home")
