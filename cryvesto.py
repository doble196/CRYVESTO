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

#ticker_list = [ 'BTC-USD','ETH-USD','BNB-USD','SOL-USD','AVAX-USD','DOT-USD','DOGE-USD', 'EXIT']
#etf_list = ['SPY', 'VTWO', 'IYW', 'ARKK', 'QQQ', 'EXIT']
#etfs=['SPY', 'IYW', 'QQQ', 'RYT', 'IETC', 'IWM', 'BND','ARKK','RPV']

ticker_list = { 'BTC-USD': 'Bitcoin',
                'ETH-USD': 'Ethereum',
                'BNB-USD': 'Binance Coin',
                'SOL-USD': 'Solana',
                'AVAX-USD': 'Avalanche',
                'DOT-USD': 'Polkadot',
                'DOGE-USD': 'Dogecoin'
}


etf_list={'SPY': 'S&P 500',
    'IYW':'iShares U.S. Technology',
    'QQQ': 'Nasdaq 100',
    'RYT': 'Invesco S&P 500 Equal Weight Technology',
    'IETC': 'iShares Evolved U.S. Technology',
    'IWM': 'iShares Russell 2000',
    'BND': 'Vanguard Total Bond Market',
    'ARKK': 'Ark Innovation',
    'RPV': 'Invesco S&P500 Pure Value'
    }
exit_str=['EXIT', 'exit', 'x', 'X']

x='''
_____________________________________
            CRYVESTO
A SMART WAY TO BUILD YOUR PORTFOLIO
_____________________________________'''
print(x)

# ask the user for the cryptos s/he wants to put in his/her portfolio. a max of 2 is allowed
# you can exit by entering EXIT, x, X, exit

try_again=1
while try_again:
    print('\nLIST OF CRYPTOS TO CHOOSE FROM')
    print('______________________________')
    for tck, desc in ticker_list.items(): print (f'{tck}  {desc} ')

    tickers_crypto = list(map(str, input(f"\nPick upto 2 Crypto Symbols (Hint- enter tickers space-seperated like ETH-USD BTC-USD) from this list (EXIT to quit): ").split()))
    
    #tickers_crypto = list(map(str, input(f"For your Portfolio, pick a max of 2 Cryptos from the following list:\n{ticker_list[:-1]}, EXIT to exit): ").split()))
#    if tickers_crypto in exit_str:
    if tickers_crypto[0] in exit_str:
        print('Thank you for visiting!!')
        exit()
    print (f'Your selection is {tickers_crypto}')
    for i in tickers_crypto:
        if i in ticker_list.keys() and len(tickers_crypto) < 3 :
            try_again=0
        else:
            try_again=1
            if len(tickers_crypto) >2:
                print ("Don't get Greedy now...Only UPTO 2 tickers please!!!")
            else:
                print("Please enter the correct ticker symbol or EXIT to quit")
            break

#Do a Four Factor Analysis on each of the Cryptos selected           
for crypto in tickers_crypto:
    ff.ffanalyse(crypto)
    #ca.analyse(tickers)

# ask the user for the ETFs s/he wants to put in his/her portfolio. a max of 3 is allowed
# you can exit by entering EXIT, x, X, exit
print('___________________________________________________________________________________________________________')
print (f"Now that you have seen the behavior of {tickers_crypto}  \nLet's begin to build out your portfolio by choosing some funds for obtaining a balance" )
print('__________________________________________________________________________________________________________')
try_again=1
while try_again:
    print('LIST OF FUNDS TO CHOOSE FROM')
    print('______________________________')

    for tck, desc in etf_list.items(): print (f'{tck}\t{desc} ')

    tickers = list(map(str, input(f"\nFor your Portfolio, pick a max of 3 ETFs from this list (EXIT to quit): ").split()))
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
    #Do Beta and Sharpe Ratio analysis
    tc.xact(tickers_crypto, tickers, etf_list)
    resp = questionary.text("Type Y to change the ETF selection, ENTER to continue..").ask()
    if resp == 'Y' or resp == 'y':
        try_again=1

#Get ready for Simulation   
curr_year =dt.datetime.now().year

start_date = pd.Timestamp(str(curr_year)+'-01-01', tz='America/New_York').isoformat()
end_date = pd.Timestamp(str(curr_year)+'-01-01', tz='America/New_York').isoformat()

num_of_years_of_data =3
num_of_years_of_projection = 2

#Now ready to do weightage
# ask the user to enter the weightage of cryptos and ETFs selected above
# it should TOTAL 1.
try_again=1
print('___________________________________________________________________________________________________________')
print (f"Now that you have seen the behavior of {tickers_crypto} and how it stacks up against {tickers} funds \nLet's continue to build out your portfolio by assigning weights to the portfolio elements" )
print('__________________________________________________________________________________________________________')
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

        #Run Montecarlo Simulation on the portfolio with the Cryptos and ETFs selected above    
        mc.run_montecarlo(tickers_crypto, tickers, num_of_years_of_data, num_of_years_of_projection, weight)
        resp = questionary.text("Type Y to change the allocation of the portfolio, ENTER to continue").ask()
        if resp == 'Y' or resp=='y':
            try_again =1
        else:
            try_again = 0
    