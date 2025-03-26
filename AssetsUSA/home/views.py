from django.shortcuts import render

def home(request):
    """View function for the home page of the site."""
    # Data is now provided by context processor
    return render(request, 'home/index.html')

def stocks(request):
    """View function for the stocks page."""
    return render(request, 'home/stocks.html')

def real_estate(request):
    """View function for the real estate page."""
    return render(request, 'home/real_estate.html')

def crypto(request):
    """View function for the cryptocurrency page."""
    return render(request, 'home/crypto.html')

def farmland(request):
    """View function for the farmland page."""
    return render(request, 'home/farmland.html')

def gold(request):
    """View function for the gold page."""
    return render(request, 'home/gold.html')

def treasury_bonds(request):
    """View function for the treasury bonds page."""
    return render(request, 'home/treasury_bonds.html')

def sp500_pe_ratio(request):
    """View function for the S&P 500 PE Ratio page."""
    return render(request, 'home/sp500_pe_ratio.html')

def stocks_percentage(request):
    """View function for the Stocks as Percentage of Total Assets page."""
    return render(request, 'home/stocks_percentage.html')

def stocks_gdp(request):
    """View function for the Stocks as Percentage of GDP page."""
    return render(request, 'home/stocks_gdp.html')

def sp500_percentage(request):
    """View function for the S&P 500 as Percentage of Total Stock Market page."""
    return render(request, 'home/sp500_percentage.html')

def top20_percentage(request):
    """View function for the Top 20 Stocks as Percentage of Total Stock Market page."""
    return render(request, 'home/top20_percentage.html')

def stocks_pe_ratio(request):
    """View function for the Total Stock Market PE Ratio page."""
    return render(request, 'home/stocks_pe_ratio.html')

def basic_materials_percentage(request):
    """View function for the Basic Materials as Percentage of Total Stock Market page."""
    return render(request, 'home/basic_materials_percentage.html')

def communication_services_percentage(request):
    """View function for the Communication Services as Percentage of Total Stock Market page."""
    return render(request, 'home/communication_services_percentage.html')

def consumer_cyclical_percentage(request):
    """View function for the Consumer Cyclical as Percentage of Total Stock Market page."""
    return render(request, 'home/consumer_cyclical_percentage.html')

def consumer_defensive_percentage(request):
    """View function for the Consumer Defensive as Percentage of Total Stock Market page."""
    return render(request, 'home/consumer_defensive_percentage.html')

def energy_percentage(request):
    """View function for the Energy as Percentage of Total Stock Market page."""
    return render(request, 'home/energy_percentage.html')

def financial_services_percentage(request):
    """View function for the Financial Services as Percentage of Total Stock Market page."""
    return render(request, 'home/financial_services_percentage.html')

def healthcare_percentage(request):
    """View function for the Healthcare as Percentage of Total Stock Market page."""
    return render(request, 'home/healthcare_percentage.html')

def industrials_percentage(request):
    """View function for the Industrials as Percentage of Total Stock Market page."""
    return render(request, 'home/industrials_percentage.html')

def real_estate_sector_percentage(request):
    """View function for the Real Estate as Percentage of Total Stock Market page."""
    return render(request, 'home/real_estate_sector_percentage.html')

def technology_percentage(request):
    """View function for the Technology as Percentage of Total Stock Market page."""
    return render(request, 'home/technology_percentage.html')

def utilities_percentage(request):
    """View function for the Utilities as Percentage of Total Stock Market page."""
    return render(request, 'home/utilities_percentage.html')
