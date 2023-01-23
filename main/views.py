from django.shortcuts import render
from django.views.generic import ListView

from .models import *


class HomeMain(ListView):
    model = Category
    template_name = 'main/home.html'
    context_object_name = 'category'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = Product.objects.filter(is_published=True)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return Category.objects.all()


class CatalogMain(ListView):
    model = Category
    template_name = 'main/catalog.html'
    context_object_name = 'category'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = Product.objects.filter(is_published=True)
        context['title'] = 'Каталог'
        return context

    def get_queryset(self):
        return Category.objects.all()


def about(request):
    return render(request, 'main/info.html')


def korzina(request):
    return render(request, 'main/korzina.html')