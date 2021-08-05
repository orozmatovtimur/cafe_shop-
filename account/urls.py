from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    # path("register/", views.register_request, name="register"),
    # path("login/", views.login_request, name="login"),
    path("logout/", logout_request, name="logout"),

]