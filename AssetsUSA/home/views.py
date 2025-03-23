from django.shortcuts import render
from django.db import connection
import json
# Create your views here.
def home(request):
    """View function for the home page of the site."""
    
    # Define asset types
    asset_types = [
        'commercial_real_estate',
        'crypto',
        'farmland',
        'residential_real_estate',
        'stock_market_cap',
        'treasury_bonds'
    ]
    
    context = {}
    
    for asset_type in asset_types:
        # Query the database
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT year, market_cap FROM {asset_type} ORDER BY year")
            rows = cursor.fetchall()
            
            years = [row[0] for row in rows]
            values = [float(row[1]) for row in rows]
        
        # Add to context
        context[f'{asset_type}_years'] = years
        context[f'{asset_type}_values'] = values
        
        # Also add JSON-formatted data for the template
        if asset_type == 'stock_market_cap':
            context['years_json'] = json.dumps(years)
            context['market_caps_json'] = json.dumps(values)
    
    return render(request, 'home/index.html', context)
