from django.contrib.auth.views import LogoutView
from django.urls import path

# from account.views import logout_request
from main import views
from main.views import *

urlpatterns = [
    path('home/', MainPageView.as_view(), name='home'),
    path('<str:slug>/', ProductListView.as_view(), name='list'),
    path('product/<int:id>/', ProductDetailView.as_view(), name='detail'),
    path('product/create/', ProductCreateView.as_view(), name='create_dish'),
    path('product/update/<int:id>/', ProductUpdateView.as_view(), name='update_dish'),
    path('product/delete/<int:id>/', ProductDeleteView.as_view(), name='delete_dish'),
    path('search', SearchListView.as_view(), name='search'),

    # cart urls
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/', views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/', views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/', views.cart_detail, name='cart_detail'),

]

