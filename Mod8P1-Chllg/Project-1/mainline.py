import pandas  as pd
import questionary
import fire
import fourfactor as ff
import cryptoanalysis as ca
import xactcryptos as tc
import MC_simulation as mc
import datetime as dt

#Main CLI for the CRYVESTO application
#initialize the arrays and ticker lists

tickers=[]
tickers_crypto=[]
weight=[]

ticker_list = ['BTC-USD','ETH-USD','BNB-USD','SOL-USD','AVAX-USD','DOT-USD','DOGE-USD', 'EXIT']
etf_list = ['SPY', 'VTWO', 'IYW', 'ARKK', 'QQQ', 'EXIT']
exit_str=['EXIT', 'exit', 'x', 'X']

x='''
Build a Portfolio with CRYPTOS and ETFs.\n
You get to choose the weightage of each to obtain a certain performance of the Portfolio\n'''
print(x)

# ask the user for the cryptos s/he wants to put in his/her portfolio. a max of 2 is allowed
# you can exit by entering EXIT, x, X, exit

try_again=1
while try_again:
    
    tickers_crypto = list(map(str, input(f"For your Portfolio, pick a max of 2 Cryptos from the following list:\n{ticker_list[:-1]}, EXIT to exit): ").split()))
#    if tickers_crypto in exit_str:
    if tickers_crypto[0] in exit_str:
        print('Thank you for visiting!!')
        exit()
    print (f'Your selection is {tickers_crypto}')
    for i in tickers_crypto:
        if i in ticker_list and len(tickers_crypto) < 3 :
            try_again=0
        else:
            try_again=1
            if len(tickers_crypto) >2:
                print ("Don't get Greedy now...Only UPTO 2 tickers please!!!")
            else:
                print("Please enter the correct ticker symbol or EXIT to quit")
            break
# ask the user for the ETFs s/he wants to put in his/her portfolio. a max of 3 is allowed
# you can exit by entering EXIT, x, X, exit
try_again=1
while try_again:
    tickers = list(map(str, input(f"For your Portfolio, pick a max of 3 ETFs from the following list:\n{etf_list[:-1]} (EXIT to quit) : ").split()))
    if tickers[0] in exit_str:
        print('Thank you for visiting!!')
        exit()
    print (f'Your selection is {tickers}')
    for i in tickers:
        if i in etf_list and len(tickers) < 4 :
            try_again=0
        else:
            if len(tickers) >3:
                print ("Please...Only UPTO 3 ETFs!!!")
            try_again=1
            print("Please enter the correct ticker symbol or EXIT to quit")
            break
# ask the user to enter the weightage of cryptos and ETFs selected above
# it should TOTAL 1.

try_again=1
while try_again:
    weight = list(map(float, input(f"Enter weightage (Hint: .05 for 5%, .3 for 30%) for {tickers_crypto+tickers}. Weightage MUST total 1 : " ).split()))
    
    if len(weight) != len(tickers_crypto+tickers): 
        print ("Please enter weights for all the funds")
        try_again=1
    elif sum(weight) != float(1):
        print(f'Sum of weights is {sum(weight)}')
        print("Please make sure the sum of all the weights adds upto 1")
        try_again=1
    else:
        try_again=0
#Do a Four Factor Analysis on each of the Cryptos selected           
for crypto in tickers_crypto:
    ff.ffanalyse(crypto)
    #ca.analyse(tickers)

#Do Beta and Sharpe Ratio analysis
tc.xact(tickers_crypto, tickers)

#Get ready for Simulation   
curr_year =dt.datetime.now().year

start_date = pd.Timestamp(str(curr_year)+'-01-01', tz='America/New_York').isoformat()
end_date = pd.Timestamp(str(curr_year)+'-01-01', tz='America/New_York').isoformat()

num_of_years_of_data =3
num_of_years_of_projection = 2

#Run Montecarlo Simulation on the portfolio with the Cryptos and ETFs selected above    
mc.run_montecarlo(tickers_crypto, tickers, num_of_years_of_data, num_of_years_of_projection, weight)
    