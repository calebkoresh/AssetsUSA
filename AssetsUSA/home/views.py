from django.shortcuts import render

def home(request):
    """View function for the home page of the site."""
    # Data is now provided by context processor
    return render(request, 'home/index.html')
