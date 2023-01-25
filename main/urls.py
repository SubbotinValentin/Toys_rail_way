from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import *


urlpatterns = [
    path('', HomeMain.as_view(), name='home'),
    path('catalog/', CatalogMain.as_view(), name='catalog'),
    path('catalog/<slug:cat_slug>', ProductList.as_view(), name='cat_slug'),
    path('prod/<slug:prod_slug>/', ProductDetail.as_view(), name='prod'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)