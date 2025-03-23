from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('stocks/', views.stocks, name='stocks'),
    path('real-estate/', views.real_estate, name='real_estate'),
    path('crypto/', views.crypto, name='crypto'),
    path('farmland/', views.farmland, name='farmland'),
    path('gold/', views.gold, name='gold'),
    path('treasury-bonds/', views.treasury_bonds, name='treasury_bonds'),
] 