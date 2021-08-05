from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

# from account.views import logout_request
from account.views import logout_request
from main.views import *

urlpatterns = [
    path('home/', MainPageView.as_view(), name='home'),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", logout_request, name="logout"),
    path('dish/create/', DishCreateView.as_view(), name='create_dish'),
    path('dish/update/<int:id>/', DishUpdateView.as_view(), name='update_dish'),
    path('dish/delete/<int:id>/', DishDeleteView.as_view(), name='delete_dish'),

]

