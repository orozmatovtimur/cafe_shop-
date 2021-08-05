from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", logout_request, name="logout"),

]