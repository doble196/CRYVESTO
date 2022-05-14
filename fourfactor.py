import pandas as pd
import pandas_datareader as reader
import datetime as dt
import statsmodels.api as sm
import questionary

def ffanalyse(tkr, start, end):
    #print(f'This is FOUR FACTOR ANALYSIS with {tkr}\n')

    #tkr='BTC-USD'
    funds=[tkr]
    fundsret=reader.get_data_yahoo(funds, start,end)['Adj Close'].pct_change()
    fundsret_mtl = fundsret.resample('M').agg(lambda x:(x+1).prod() -1)
    #fundsret_mtl.head()
    fundsret_mtl = fundsret_mtl[1:]
    #fundsret_mtl.shape

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

    if beta_s > beta_v:
        print('____________________________________________________________________________________________________________________________________________________')
        print (f'Based upon Famma French, {tkr} is behaving like Growth stock, you may want to balance your Portfolio using some Value and Broader Market elements')
        print('____________________________________________________________________________________________________________________________________________________')

    resp=questionary.text("Type Y to see detailed analysis, or ENTER to continue? ").ask()
    if resp == 'Y' or resp=='y':
        print(results.summary())
        questionary.text("Type ENTER Key TO Proceed...? ").ask()
    
