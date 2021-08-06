from cart.cart import Cart
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin


from main.forms import *
from main.models import *


class MainPageView(ListView):
    model = Category
    template_name = 'home.html'
    context_object_name = 'categories'


class ProductListView(ListView):
    model = Product
    template_name = 'list_dish.html'
    context_object_name = 'products'
    paginate_by = 1

    def get_queryset(self):
        queryset = super().get_queryset()
        slug = self.kwargs.get('slug')
        queryset = queryset.filter(category__slug=slug)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.kwargs.get('slug')
        return context

    def get_success_url(self):
        return reverse('home')


class IsAdminCheckMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_superuser


class ProductDetailView(DetailView):
    model = Product
    template_name = 'detail_dish.html'
    context_object_name = 'products'
    pk_url_kwarg = 'id'

    def get_success_url(self):
        return reverse('home')


class ProductCreateView(IsAdminCheckMixin, CreateView):
    model = Product
    template_name = 'create_dish.html'
    form_class = CreateDishForm
    context_object_name = 'product_form'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_form'] = self.get_form(self.get_form_class())
        return context

    def get_success_url(self):
        return reverse('home')


class ProductUpdateView(IsAdminCheckMixin, UpdateView):
    model = Product
    template_name = 'update_dish.html'
    form_class = UpdateDishForm
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_form'] = self.get_form(self.get_form_class())
        return context


class ProductDeleteView(IsAdminCheckMixin, DeleteView):
    model = Product
    template_name = 'delete_dish.html'
    pk_url_kwarg = 'id'

    def get_success_url(self):
        return reverse('home')


class SearchListView(ListView):
    model = Product
    template_name = 'search_results.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        print(queryset.filter(name=q))

        if not q:
            return Product.objects.none()
        queryset = queryset.filter(Q(name__icontains=q) |
                                   Q(description__icontains=q))
        print(queryset)
        return queryset


@login_required()
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("home")



@login_required()
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required()
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required()
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required()
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required()
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')

