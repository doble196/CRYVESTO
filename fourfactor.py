import pandas as pd
import pandas_datareader as reader
import datetime as dt
import statsmodels.api as sm
import questionary
import xactcryptos as tc

#This function performs the Famma French Four Factor analysis on for the Ticker (tkr)
#Arguments:
# - tkr: ticker for which FF analysis needs be performed
# - start: start date for historical data
# - end: end date for historical data

def ffanalyse(tkr, start, end):
    #print(f'FAMMA FRENCH FOUR FACTOR ANALYSIS for {tkr}')

    #tkr='BTC-USD'
    funds=[tkr]
    # get Data for tkr from Yahoo finance using get_data from xactcryptos
    #fundsret=reader.get_data_yahoo(funds, start,end)['Adj Close'].pct_change()
    fundsret = tc.get_data(funds, start, end)['Adj Close']
    fundsret_mtl = fundsret.resample('M').agg(lambda x:(x+1).prod() -1)
    #fundsret_mtl.head()
    fundsret_mtl = fundsret_mtl[1:]
    #fundsret_mtl.shape

    #get the factor data from Famma French library
    factors= reader.DataReader('F-F_Research_Data_Factors', 'famafrench',start,end)[0]
    factors['mom']=reader.DataReader('F-F_Momentum_Factor', 'famafrench',start,end)[0]
    factors= factors[1:]
    fundsret_mtl = fundsret_mtl[:len(fundsret_mtl)-1]
    fundsret_mtl.index = factors.index
    merge = pd.merge(fundsret_mtl, factors, on='Date')
    merge[['Mkt-RF','SMB','HML', 'RF','mom']] = merge[['Mkt-RF','SMB','HML', 'RF', 'mom']]/100
    merge[tkr+'-RF']=merge[tkr] - merge.RF

    #dependent variable
    y=merge[tkr+'-RF']
    #independent variables
    X=merge[['Mkt-RF','SMB','HML','mom']]
    #Define constant
    X_sm = sm.add_constant(X)

    #now, the model-OLS - Ordinary Squares/d
    model = sm.OLS(y,X,sm)
    results=model.fit()
    beta_m, beta_s, beta_v, beta_mom = results.params

    # Based upon the relative Betas, decide the behavior of the Ticker

    if beta_s > beta_v and beta_s > beta_m:
        print('____________________________________________________________________________________________________________________________________________________')
        print (f'Based upon Famma French, {tkr} is behaving more like a Growth stock, you may want to balance your Portfolio using some Value and Broader Market elements')
        print('____________________________________________________________________________________________________________________________________________________')
    if beta_v > beta_s and beta_v > beta_m:
        print('____________________________________________________________________________________________________________________________________________________')
        print (f'Based upon Famma French, {tkr} is behaving more like a Value stock, you may want to balance your Portfolio using some Growth and Broader Market elements')
        print('____________________________________________________________________________________________________________________________________________________')
    if beta_m > beta_v and beta_m > beta_s:
        print('____________________________________________________________________________________________________________________________________________________')
        print (f'Based upon Famma French, {tkr} is behaving more in line with Market than other factors, you may want to add Value and Growth stocks ')
        print('____________________________________________________________________________________________________________________________________________________')

    #Display detailed FF Analysis, only if the user wants.
    resp=questionary.text("Type Y to see detailed analysis, or ENTER to continue? ").ask()
    if resp == 'Y' or resp=='y':
        print(results.summary())
        questionary.text("Type ENTER Key TO Proceed...? ").ask()
    
