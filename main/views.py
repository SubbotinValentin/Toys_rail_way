from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth import authenticate, login

from cart.forms import CartAddProductForm

from .models import *


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


def about(request):
    return render(request, 'main/about.html')