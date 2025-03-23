from django.db import connection
import json

def asset_data(request):
    """Context processor that provides asset data for all templates."""
    
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
    all_years = []
    
    for asset_type in asset_types:
        # Query the database
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT year, market_cap FROM {asset_type} ORDER BY year")
            rows = cursor.fetchall()
            
            years = [row[0] for row in rows]
            values = [float(row[1]) for row in rows]
        
        # Add to context
        context[f'{asset_type}_years'] = json.dumps(years)
        context[f'{asset_type}_values'] = json.dumps(values)
        
        # Store Chart.js friendly format
        context[f'{asset_type}_chart_data'] = json.dumps({
            'labels': years,
            'datasets': [{
                'label': asset_type.replace('_', ' ').title(),
                'data': values,
                'borderColor': get_color_for_asset(asset_type),
                'fill': False
            }]
        })
        
        # Update all_years to have the most complete set
        if len(years) > len(all_years):
            all_years = years
    
    # Add global years data
    context['all_years_json'] = json.dumps(all_years)
    
    return context

def get_color_for_asset(asset_type):
    """Return a color for each asset type."""
    colors = {
        'commercial_real_estate': 'rgb(255, 99, 132)',
        'crypto': 'rgb(54, 162, 235)',
        'farmland': 'rgb(255, 206, 86)',
        'residential_real_estate': 'rgb(75, 192, 192)',
        'stock_market_cap': 'rgb(153, 102, 255)',
        'treasury_bonds': 'rgb(255, 159, 64)'
    }
    return colors.get(asset_type, 'rgb(0, 0, 0)')