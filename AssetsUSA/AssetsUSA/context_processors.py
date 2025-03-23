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
        'treasury_bonds',
        'gdp',
        'gold'
    ]
    
    # Initialize data structure
    yearly_data = {}
    all_years = set()
    
    # First pass: collect all years and data
    for asset_type in asset_types:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT year, market_cap FROM {asset_type} ORDER BY year")
            rows = cursor.fetchall()
            
            for year, value in rows:
                all_years.add(year)
                if year not in yearly_data:
                    yearly_data[year] = {}
                yearly_data[year][asset_type] = float(value)
    
    # Convert to sorted list of years
    all_years = sorted(list(all_years))
    
    # Prepare context with complete data structure
    context = {
        'all_years_json': json.dumps(all_years)
    }
    
    # Create datasets ensuring null values for missing years
    for asset_type in asset_types:
        data_points = []
        for year in all_years:
            value = yearly_data.get(year, {}).get(asset_type, None)
            data_points.append(value)
            
        context[f'{asset_type}_chart_data'] = json.dumps({
            'labels': all_years,
            'datasets': [{
                'label': asset_type.replace('_', ' ').title(),
                'data': data_points
            }]
        })
    
    return context