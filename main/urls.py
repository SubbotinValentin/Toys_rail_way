from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import *


urlpatterns = [
    path('', HomeMain.as_view(), name='home'),
    path('catalog/', CatalogMain.as_view(), name='catalog'),
    path('catalog/<slug:cat_slug>', CatalogList.as_view(), name='cat_slug'),
    path('post/<slug:post_slug>/', PostProduct.as_view(), name='post'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('korzina/', korzina, name='korzina'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)