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
    path('sp500-pe-ratio/', views.sp500_pe_ratio, name='sp500_pe_ratio'),
    path('stocks-percentage/', views.stocks_percentage, name='stocks_percentage'),
    path('stocks-gdp/', views.stocks_gdp, name='stocks_gdp'),
    path('sp500-percentage/', views.sp500_percentage, name='sp500_percentage'),
    path('top20-percentage/', views.top20_percentage, name='top20_percentage'),
    path('stocks-pe-ratio/', views.stocks_pe_ratio, name='stocks_pe_ratio'),
    path('basic-materials-percentage/', views.basic_materials_percentage, name='basic_materials_percentage'),
    path('communication-services-percentage/', views.communication_services_percentage, name='communication_services_percentage'),
    path('consumer-cyclical-percentage/', views.consumer_cyclical_percentage, name='consumer_cyclical_percentage'),
    path('consumer-defensive-percentage/', views.consumer_defensive_percentage, name='consumer_defensive_percentage'),
    path('energy-percentage/', views.energy_percentage, name='energy_percentage'),
    path('financial-services-percentage/', views.financial_services_percentage, name='financial_services_percentage'),
    path('healthcare-percentage/', views.healthcare_percentage, name='healthcare_percentage'),
    path('industrials-percentage/', views.industrials_percentage, name='industrials_percentage'),
    path('real-estate-sector-percentage/', views.real_estate_sector_percentage, name='real_estate_sector_percentage'),
    path('technology-percentage/', views.technology_percentage, name='technology_percentage'),
    path('utilities-percentage/', views.utilities_percentage, name='utilities_percentage'),
] 