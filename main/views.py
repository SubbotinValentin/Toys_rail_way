from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import logout, login

from cart.forms import CartAddProductForm

from .models import *
from .forms import *


class HomeMain(ListView):
    model = Category
    template_name = 'main/home.html'
    context_object_name = 'category'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context


class CatalogMain(ListView):
    model = Category
    template_name = 'main/product/catalog.html'
    context_object_name = 'category'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = Product.objects.filter(is_published=True)
        context['title'] = 'Каталог'
        return context

    def get_queryset(self):
        return Category.objects.all()


class ProductList(ListView):
    model = Category
    template_name = 'main/product/catalog.html'
    context_object_name = 'category'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = Product.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)
        context['title'] = 'Каталог'
        return context

    def get_queryset(self):
        return Category.objects.all()


class ProductDetail(DetailView):
    model = Product
    template_name = 'main/product/post.html'
    slug_url_kwarg = 'prod_slug'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_product_form'] = CartAddProductForm()
        context['title'] = context['product']
        return context


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Вход'
        return context

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


def korzina(request):
    return render(request, 'main/korzina.html')