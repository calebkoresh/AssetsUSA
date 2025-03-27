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

def sp500_market_cap(request):
    """View function for the S&P 500 Market Cap page."""
    return render(request, 'home/sp500_market_cap.html')

def shiller_ratio(request):
    """View function for the Shiller PE Ratio (CAPE) page."""
    return render(request, 'home/shiller_ratio.html')

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

def total_assets(request):
    """View function for the Total Asset Pool page."""
    return render(request, 'home/total_assets.html')

def gdp_chart(request):
    """View function for the GDP by Year page."""
    return render(request, 'home/gdp_chart.html')

def real_estate_percentage(request):
    """View function for the Real Estate as Percentage of Total Assets page."""
    return render(request, 'home/real_estate_percentage.html')

def real_estate_gdp(request):
    """View function for the Real Estate as Percentage of GDP page."""
    return render(request, 'home/real_estate_gdp.html')

def residential_real_estate_percentage(request):
    """View function for the Residential Real Estate as Percentage of Total Assets page."""
    return render(request, 'home/residential_real_estate_percentage.html')

def residential_real_estate_gdp(request):
    """View function for the Residential Real Estate as Percentage of GDP page."""
    return render(request, 'home/residential_real_estate_gdp.html')

def commercial_real_estate_percentage(request):
    """View function for the Commercial Real Estate as Percentage of Total Assets page."""
    return render(request, 'home/commercial_real_estate_percentage.html')

def commercial_real_estate_gdp(request):
    """View function for the Commercial Real Estate as Percentage of GDP page."""
    return render(request, 'home/commercial_real_estate_gdp.html')

def crypto_percentage(request):
    """View function for the Cryptocurrency as Percentage of Total Assets page."""
    return render(request, 'home/crypto_percentage.html')

def bitcoin_percentage(request):
    """View function for the Bitcoin as Percentage of Crypto Market Cap page."""
    return render(request, 'home/bitcoin_percentage.html')

def ethereum_percentage(request):
    """View function for the Ethereum as Percentage of Crypto Market Cap page."""
    return render(request, 'home/ethereum_percentage.html')

def other_crypto_percentage(request):
    """View function for the Other Cryptocurrencies as Percentage of Crypto Market Cap page."""
    return render(request, 'home/other_crypto_percentage.html')

def gold_percentage(request):
    """View function for the Gold as Percentage of Total Assets page."""
    return render(request, 'home/gold_percentage.html')

def treasury_bonds_percentage(request):
    """View function for the Treasury Bonds as Percentage of Total Assets page."""
    return render(request, 'home/treasury_bonds_percentage.html')

def total_real_estate_market_cap(request):
    """View function for the Total Real Estate Market Cap page."""
    return render(request, 'home/total_real_estate_market_cap.html')

def residential_real_estate_market_cap(request):
    """View function for the Residential Real Estate Market Cap page."""
    return render(request, 'home/residential_real_estate_market_cap.html')

def commercial_real_estate_market_cap(request):
    """View function for the Commercial Real Estate Market Cap page."""
    return render(request, 'home/commercial_real_estate_market_cap.html')

def gold_market_cap(request):
    """View function for the Gold Market Cap page."""
    return render(request, 'home/gold_market_cap.html')

def treasury_bonds_market_cap(request):
    """View function for the Treasury Bonds Market Cap page."""
    return render(request, 'home/treasury_bonds_market_cap.html')

def crypto_market_cap(request):
    """View function for the Cryptocurrency Market Cap page."""
    return render(request, 'home/crypto_market_cap.html')

def bitcoin_market_cap(request):
    """View function for the Bitcoin Market Cap page."""
    return render(request, 'home/bitcoin_market_cap.html')

def ethereum_market_cap(request):
    """View function for the Ethereum Market Cap page."""
    return render(request, 'home/ethereum_market_cap.html')

def other_crypto_market_cap(request):
    """View function for the Other Cryptocurrencies Market Cap page."""
    return render(request, 'home/other_crypto_market_cap.html')

def top20_stocks_market_cap(request):
    """View function for the Top 20 Stocks Market Cap page."""
    return render(request, 'home/top20_stocks_market_cap.html')

def basic_materials_market_cap(request):
    """View function for the Basic Materials Market Cap page."""
    return render(request, 'home/basic_materials_market_cap.html')

def communication_services_market_cap(request):
    """View function for the Communication Services Market Cap page."""
    return render(request, 'home/communication_services_market_cap.html')

def consumer_defensive_market_cap(request):
    """View function for the Consumer Defensive Market Cap page."""
    return render(request, 'home/consumer_defensive_market_cap.html')

def energy_market_cap(request):
    """View function for the Energy Market Cap page."""
    return render(request, 'home/energy_market_cap.html')

def financial_services_market_cap(request):
    """View function for the Financial Services Market Cap page."""
    return render(request, 'home/financial_services_market_cap.html')

def healthcare_market_cap(request):
    """View function for the Healthcare Market Cap page."""
    return render(request, 'home/healthcare_market_cap.html')

def industrials_market_cap(request):
    """View function for the Industrials Market Cap page."""
    return render(request, 'home/industrials_market_cap.html')

def real_estate_sector_market_cap(request):
    """View function for the Real Estate Sector Market Cap page."""
    return render(request, 'home/real_estate_sector_market_cap.html')

def technology_market_cap(request):
    """View function for the Technology Market Cap page."""
    return render(request, 'home/technology_market_cap.html')

def utilities_market_cap(request):
    """View function for the Utilities Market Cap page."""
    return render(request, 'home/utilities_market_cap.html')
