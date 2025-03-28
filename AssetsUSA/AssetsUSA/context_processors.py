from django.db import connection
import json
import pandas as pd
import os

def asset_data(request):
    """Context processor that provides asset data for all templates."""
    
    # Define asset types
    asset_types = [
        'commercial_real_estate',
        'crypto',
        'residential_real_estate',
        'stock_market_cap',
        'treasury_bonds',
        'gdp',
        'gold',
        'top20_stocks',
        'sp500',
        'stocks_basic_materials',
        'stocks_comm_services',
        'stocks_consumer_cyclical',
        'stocks_consumer_defensive',
        'stocks_energy',
        'stocks_financial_services',
        'stocks_healthcare',
        'stocks_industrials',
        'stocks_real_estate',
        'stocks_tech',
        'stocks_utilities',
        'bitcoin',
        'ethereum',
        'stocks_pe',
        'sp500_pe',
        'shiller_ratio'
    ]
    
    # Get the base directory for CSV files
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_dir = os.path.join(base_dir, 'AssetsUSA', 'database')
    
    # Initialize data structure
    yearly_data = {}
    all_years = set()
    
    # First pass: collect all years and data from CSV files
    for asset_type in asset_types:
        csv_path = os.path.join(csv_dir, f"{asset_type}.csv")
        try:
            # Read the CSV file using pandas
            df = pd.read_csv(csv_path)
            
            # Process each row in the dataframe
            for _, row in df.iterrows():
                year = int(row['year'])
                value = float(row['market_cap'])
                
                all_years.add(year)
                if year not in yearly_data:
                    yearly_data[year] = {}
                yearly_data[year][asset_type] = value
        except (FileNotFoundError, pd.errors.EmptyDataError):
            # Skip if the file doesn't exist or is empty
            continue
    
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