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
