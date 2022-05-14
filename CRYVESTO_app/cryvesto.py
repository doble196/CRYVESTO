import pandas  as pd
import questionary
import fire
import fourfactor as ff
import xactcryptos as tc
import MC_simulation as mc
import datetime as dt

#Main CLI for the CRYVESTO application
#initialize the arrays and ticker lists

tickers=[]
tickers_crypto=[]
weight=[]


ticker_list = { 'BTC-USD': 'Bitcoin',
                'ETH-USD': 'Ethereum',
                'BNB-USD': 'Binance Coin',
                'DOGE-USD': 'Dogecoin'
}

etf_list={'SPY': 'S&P 500  ',
    'IYW':'iShares U.S. Technology',
    'QQQ': 'Nasdaq 100     ',
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

# Set the start and end dates for fetching the data 

end = dt.date(2022,3,31)
start = dt.date(end.year- 3, end.month, end.day)

# ask the user for the cryptos s/he wants to put in his/her portfolio. a max of 2 is allowed
# you can exit by entering EXIT, x, X, exit

try_again=1
while try_again:
    print('\nLIST OF CRYPTOS TO CHOOSE FROM')
    print('______________________________')
    for tck, desc in ticker_list.items(): print (f'{tck}  {desc} ')

    tickers_crypto = list(map(str, input(f"\nPick upto 2 Crypto Symbols (Hint- enter tickers space-seperated like ETH-USD BTC-USD) from this list (EXIT to quit): ").split()))
    
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

#Do a Four Factor Analysis on each of the Cryptos selected to find out how is this Crypto behaving           
for crypto in tickers_crypto:
    ff.ffanalyse(crypto, start, end)
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
        if i in etf_list.keys() and len(tickers) < 4 :
            try_again=0
        else:
            try_again = 1
            if len(tickers) >3:
                print ("Please...Only UPTO 3 ETFs!!!")
            else:
                print("Please enter the correct ticker symbol")
            break

    if not try_again:
        #Do Risk-Return/Beta and Sharpe Ratio analysis
        tc.do_risk_return_analysis(tickers_crypto, tickers, etf_list, start, end)
        resp = questionary.text("Type Y to change the ETF selection, ENTER to continue..").ask()
        if resp == 'Y' or resp == 'y':
            try_again=1
    
        

#Get ready for Simulation   
curr_year =dt.datetime.now().year

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
    elif sum(weight) != float(1.0):
        print(f'Sum of weights is {sum(weight)}')
        print("Please make sure the sum of all the weights adds upto 1")
        try_again=1
    else:
        try_again=0
        print('___________________________________________________________________________________________________________')

        print ('''Your projected returns are based upon historical data and our proprietary methodology, 
if you want to further finetune the analysis, you have the option to select the number of years of historical data.\n''')

        again=1
        while again:
            # Give an option to input num of years of data to be used for simulations, default is 3
            # allow 2-5 years, since Crypto data before 5 years is meaningless (as in 2022)
            inp = input("How many Years of Historical Data You Want Me To Use (Choose between 2-5)<Press ENTER for 3 years>: ") 
            if inp=='':
                num_of_years_of_data =3
                num_of_years_of_projection = 2
                again=0
                break
            inp=int(inp)
            if inp > 5 or inp < 2:
                print ('Uff... 2 - 5 years only, please!')
                again=1
            else:
                num_of_years_of_data = inp
                num_of_years_of_projection = int(inp/2)
                again=0

        #Run Montecarlo Simulation on the portfolio with the Cryptos and ETFs selected above    
        mc.run_montecarlo(tickers_crypto, tickers, num_of_years_of_data, num_of_years_of_projection, weight)

        #Give option to change the allocation of weightage
        resp = questionary.text("Type Y to change the allocation of the portfolio, ENTER to continue").ask()
        if resp == 'Y' or resp=='y':
            try_again =1
        
    