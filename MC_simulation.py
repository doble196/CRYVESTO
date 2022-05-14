import os
import pandas as pd
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi
from MCForecastTools import MCSimulation
import datetime as dt
import load_data as ld
import alpaca_trade_api as tradeapi

#%matplotlib inline


#do montecarlo simulation for the portfolio slected
#Arguments:
# - tickers_crypto: crypto tickers selected
# - tickers: tickers of the funds slecected
# - num_of_years_of_data: # of yrs of data to use for the simulation
# - num_of_years_of_projection: # of years to do the projection for
# - weight: weightage given to each ticker. when added they must total 1

def run_montecarlo(tickers_crypto, tickers, num_of_years_of_data, num_of_years_of_projection, weight):
    load_dotenv('my_api.env')
    os.getenv('ALPACA_API_KEY')

    alpaca_api_key = os.getenv('ALPACA_API_KEY')
    alpaca_secret_key = os.getenv('ALPACA_SECRET_KEY')

    curr_year =dt.datetime.now().year

# Create the Alpaca tradeapi.REST object
# YOUR CODE HERE
    alpaca_rest_obj = tradeapi.REST(
        alpaca_api_key,
        alpaca_secret_key,
        api_version='v2'
    )

    start = dt.datetime(curr_year - num_of_years_of_data, 1, 1)
    end = dt.datetime(curr_year, 1, 1)
    #tickers=['BTC-USD','SPY','VTWO', 'IYW', 'QQQ']
   # tickers_crypto=['BTC-USD', 'ETH-USD']

#LOAD FROM YAHOO
    p_yahoo=ld.load_from_yahoo(tickers_crypto, start,end)

#LOAD FROM ALPACA
    #tickers=['SPY','VTWO', 'IYW', 'QQQ']
#tickers=['SPY']
    start_date = pd.Timestamp(str(curr_year-num_of_years_of_data)+'-01-01', tz='America/New_York').isoformat()
    end_date = pd.Timestamp(str(curr_year)+'-01-01', tz='America/New_York').isoformat()

    p_alpaca=ld.load_from_alpaca(tickers, start_date,end_date)

    portfolio = pd.concat([p_yahoo, p_alpaca], axis=1).dropna()

# Configure the Monte Carlo simulation to forecast based upon num_of_years_of_data  cumulative returns
    MC_yrs_sim = MCSimulation(
    portfolio_data=portfolio,
    weights= weight,
    num_simulation=100, # to reduce time, chose 100
    num_trading_days=252 * num_of_years_of_projection
)
    
    MC_yrs_sim.calc_cumulative_return()

    MC_yrs_sim.plot_simulation()

    MC_yrs_sim.plot_distribution()

    #setup the initial investment amount so we can give the projection based upon this investment amount

    initial_investment=10000
    summary_ret = MC_yrs_sim.summarize_cumulative_return()

    #print out the results
    '''print('_______________________________________')

    print('Summary statistics from the simulations')
    print('_______________________________________')
    print(summary_ret)
    '''

    ci_lower_ten_cumulative_return = summary_ret[8] * initial_investment
    ci_upper_ten_cumulative_return = summary_ret[9] * initial_investment

# Print the result of your calculations
    print('___________________________________________________________________________________________')
    print(f'Projected Performance of ${initial_investment:,.02f} investment in the Following Portfolio that You Selected:\n')
    print('TICKER\t\tINVESTMENT\tWEIGHTAGE')
    j=0
    for i in tickers_crypto+tickers:
        print(f'{i}\t\t{initial_investment*weight[j]:,.02f}\t {weight[j]}')
        j+=1
    
    print('_________________')
    print('PROJECTED RETURNS')
    print('_________________')
    print(f"Using 95% Confidence Intervals, and {num_of_years_of_data} years of historical data, \nyour investment of ${initial_investment:,.02f} would return from ${ci_lower_ten_cumulative_return:,.02f} to ${ci_upper_ten_cumulative_return:,.02f} over the next {num_of_years_of_projection} years.")
    
