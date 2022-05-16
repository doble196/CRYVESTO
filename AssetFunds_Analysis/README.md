# FinTech Cryptocurrency Analysis of Asset Classes Using Monte Carlo Simulations 

*A FinTech project to analyze cryptocurrencies with 'CryVesto for your Portfolio'*

---

## Background
This program application is for a fintech startup serving as a crypto consulting and research firm. It compares different indicies and asset classes with an alternative asset of cryptocurrency to measure portfolio performance. It is part of a larger program analysis following the Fama-French Regression Analysis and before the user interface app to help clients make investment decisions. It utilizes a Monte Carlo Simulation app projecting returns based on analysis of major equity and fixed income asset classes with and without cryptocurrency for comparison purposes, as a viable alternate class of investment.   

In setting up this part of the analysis, consideration was given to the major asset classes in constructing a portfolio with cryptocurrencies as an alternate investment. Traditionally the 3 major classes are equities(stocks), fixed income(bonds), and cash or its equivalents like money market funds. For the purpose of this analysis after utilizing the Fama-French regression model, the major asset classes are identified with a proxy selection of ETFs. Attention is given to divide the equities into sub-classes using differing asset class indexes to reflect diversification and risk/return characteristics. The fixed income asset is the traditional asset of stability, low risk and liquidity for balancing a portfolio's risk/returns overtime. Special attention is given to a popular aggressive growth ETF composed mostly of high risk start-ups with innovative technology. We will forecast using different portfolio models and observe how each asset class performs differently in prevailing market conditions, and under certain economic events with and without cryptocurrency. 

The major equities markets are the S&P 500, NASADQ 100, Russell 2000, and S&P 500 Value indicies represented by the following ETFs: SPY, QQQ, VTWO, RPV respectively. The traditional asset of fixed income is represented by the Total Bond Market ETF(BND). Special consideration is given to ARK Innovation ETF (ARKK) as a popular aggressive growth ETF composed mostly of high risk start-ups with innovative technology. And most importantly for the limelight of our analysis a cryptocurrency ETF Bitcoin Strategy(BITO). These ETFs are selected to emulate models of benchmark indexes and key asset themes for portfolio allocation and to identify risks/returns for comparison purposes. 

This app makes forecasts by dividing the weighting of a portfolio into 5 different positions for comparison using an initial investment of $10,000 (without cryptocurrency) using various asset class combinations of stock and bond indexes. And one including cryptocurrency in the portfolio, while omitting the NASDAQ 100 index ETF QQQ to avoid asset class overlap in the summary metrics. Reasoning is that FAANG stocks comprise 33% of NASDAQ market capitalization and technology stocks added comprise over 50% market cap of the index. In the S&P 500 by comparison, FAANG holds 19% and 28% respectively. Observing that QQQ has similar summary statistics with VTWO, but a higher mean metric inline with S&P 500, it is omitted for greater asset class separation in the portfolio. As such, QQQ ETF is omitted in the portfolio weighting of portfolio_data of etf_aggr_prices for the MCSimulator. For the the same reason it is ommitted from portfolio_data of etf_crypto_prices. 

This app within the 'CryVesto' program utilizes an Alpaca API to get historical closing prices for the various proxy ETFs to compare against alternate investment ideas of ARKK and BITO ETFs. It runs a Monte Carlo Simulation with 1000 samples to forecast the portfolio performance of 1 year, as well as different portfolio asset weightings(ratios) of stock and bond returns as a constant before comparing alternate asset classes of hi-Tech aggressive growth and cryptocurrency itself. This should help clients understanding of risk assessment with a 95 percent confidence level when changing portfolio equity/bond weighting and time periods to meet goals.

The data and chart visualizations should help 'Investors' consider portfolio funding options using cryptocurrency as an alternate investment.  

Utilizing the Fama-French Regression analysis of my colleague followed by the Monte Carlo Simulator forcasting various portfolio asset ratio outcomes in a hypothetical portfolio divided by asset class. Calculating risk/return in future time narrows down the concept of asset performance and where cryptocurrency fits in a portfolio before using the client 'CryVesto App'. The MC Simulator 'CryVesto App' assist clients using a 95% confidence level for the results to determine how much Bitcoin to purchase in a portfolio to attain financial planning goals.

---

## Technologies

The software operates on python 3.9 with the installation package imports embedded with Anaconda3 installation and MCSimulation module obtained from MCForecastTools:

* [anaconda3](https://docs.anaconda.com/anaconda/install/windows/e) .

* [MCForecastTools.py](https://cdn.inst-fs-pdx-prod.inscloudgate.net/e0e08ad7-c5b3-43c1-8e7c-e7efc5f1f39c/MCForecastTools.py?token=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCIsImtpZCI6ImNkbiJ9.eyJyZXNvdXJjZSI6Ii9lMGUwOGFkNy1jNWIzLTQzYzEtOGU3Yy1lN2VmYzVmMWYzOWMvTUNGb3JlY2FzdFRvb2xzLnB5IiwidGVuYW50IjoiY2FudmFzIiwidXNlcl9pZCI6IjE1MDQyMDAwMDAwMDAxODE0MiIsImlhdCI6MTY1MDgzNzk1OSwiZXhwIjoxNjUwOTI0MzU5fQ.VVAZTpXzX9mBx6vnKocyZoIxDBXzM4T-fZ3x9YAxzvjvID_OarmksBCAVMdjKJ8v8i_Ga8KoGLhBGqvfT44IoA&content_type=text%2Fx-python) .

---

## Installation Guide

Before running the applications first activate the Conda development environment and launch JupyterLab to import the following required libraries apps. 

```python libraries

import os
import json
import requests
import pandas as pd
import hvplot.pandas
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi
from MCForecastTools import MCSimulation 
%matplotlib inline 
```

---
# Usage

This application is launched from web-based JupyterLab utilizing Pandas which is designed for data analysis to write and read code in an IDE and review results through the Python libraries. The Anaconda3 software application includes the Pandas libraries; **os, requests, json, load_dotenv, alpaca_trade_api, MCSimulation,%matplotlib inline** to utilize data frames, forecast through simulations and plot charts in an integrated Conda development environment. 

Importantly download the Alpaca API key and secret keys from *https://app.alpaca.markets/brokerage/new-account* to save in a *.env* file. It functions for holding api keys to access Alpaca API market data SDK. To use *.env* functionality **import os** and **import load_dotenv** are required to call the **load_dotenv()** function.

The program is developed in Jupyter notebooks on a **.ipny** file.  The pandas imports help the imports of **os, requests, json, load_dotenv** retrieve data from remote api's, and load them in your computor within a data frame to visualize and analyze. The JSON library is needed to work with files in the JavaScript Object Notation (JSON) format for API requests and interface with your machine. Using **numpy** library tools facilitates math calculations with large quantities of data sets to get: daily returns, risk and return metrics, standard deviation, and beta. The Pandas **%matplotlib inline** enables functions to create informative visualizations from the Pandas DataFrames and data metrics. The **import alpaca_trade_api** is required to retreive data for stock and bond simulations. The **MCSimulation** app is required to running the Monte Carlo simulation program.   

Finally the **CryVesto_ForeCast.ipynb**  program on this part of the CryVesto team project utilizes the above libraries to perform several steps in retrieving, creating, evaluating, analyzing data in order to make forecasts with cryptocurrencies focusing on Bitcoin for portfolio analysis planning . Utilizing the Fama-French Regression analysis with the Monte Carlo Simulator to calculate risk/return overtime, these steps can assist with 95-percent confidence of the results in making a determination of how much weight to place on Bitcoin investments in a portfolio to attain financial planning goals.   

```python
financial_planning_tools.ipynb
```
 

---

## Contributors

*Provided to you by digi-Borg FinTek*, 
Dane Hayes: nydane1@gmail.com

---

## License

Columbia U. Engineering
