# FinTech Financial Planning Using Monte Carlo Simulations and API's

*Welcome to my FinTech project as a 'Financial Planner for Retirement Portfolios'*

---

## Background
This project is for a fintech startup serving as a consulting firm for a Credit Union, after winning its first contract. After consultation with the credit union CTO, the board requires financial planning for CU members with an 'Emergency Fund' and another for a 'Retirement Fund'. 

To meet requirements, 2 different programming analysis tools were designed for this project: the 1st is used to plan an emergency fund and the 2nd is for retirement planning. The 'Emergency Fund'program seeks to aid the members with a savings plan for funding unexpected expenses, while the 'Retirement Fund' seeks to project performance by forcasting at a 95% confidence level to attain portfolio goals for retirement. 

The program planner for emergency funding assumes CU members average monthly income of $12K with a porfolio of crypto currency, stocks and bonds. We'll assume each member holds 1.2 Bitcoins and 5.3 Ethereum coins and get prices through API JSON. Its goal is to save 3 times their income for the 'Emergency Fund'. 

The retirement program utilizes an Alpaca API to get historical closing prices for stocks using an index ETF(SPY) and bond index(AGG) to simulate future market returns in the retirement portfolio. We’ll run a Monte Carlo simulation with 500 samples to forecast the portfolio performance of 30 year and 10 year time periods, as well as different porfolio ratios(weighting) of stock and bond returns. This should help members with assessing risks at 95% confidence level when changing portfolio stock/bond weighting and time periods to meet goals.

These programs give users a mix to visually offer CU members options in portfolio funding management. The data and chart visualations should help 'Investment Representatives' discuss porfolio funding options with CU members.  

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
import requests
import json
import pandas as pd
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi
from MCForecastTools import MCSimulation 
%matplotlib inline 
```

---
# Usage

This application is launched from web-based JupyterLab utilizing Pandas which is designed for data analysis to write and read code in an IDE and review results through the Python libraries. The Anaconda3 software application includes the Pandas libraries; **os, requests, json, load_dotenv, alpaca_trade_api, MCSimulation,%matplotlib inline** to utilize data frames, forecast through simulations and plot charts in an integrated Conda development environment. 

Importantly download the Alpaca API key and secret keys from *https://app.alpaca.markets/brokerage/new-account* to save in a *.env* file. It functions for holding api keys to access Alpaca API market data SDK. To use *.env* functionality **import os** and **import load_dotenv** are required to call the **load_dotenv()** function.

The program is developed in Jupyter notebooks on a **.ipny** file.  The pandas imports help the imports of **os, requests, json, load_dotenv** retrieve data from remote API's, and load them in your computor within a data frame to visualize and analyze. The JSON library is needed to work with files in the JavaScript Object Notation (JSON) format for API requests and interface with your machine. Using **numpy** library tools facilitates math calculations with large quantities of data sets to get: daily returns, risk and return metrics, standard deviation, and beta. The Pandas **%matplotlib inline** enables functions to create informative visualizations from the Pandas DataFrames and data metrics. The **import alpaca_trade_api** is required to retreive data for stock and bond simulations. The **MCSimulation** app is required to running the Monte Carlo simulation program.   

Finally the **financial_planning_tools.ipynb** program utilizing the above libraries has several steps to retrieve, create, evaluate, analyze data and make forcasts for portfolio planning. Through these steps a determination is made for CU members to adequately access their financial planning goals.   

```python
financial_planning_tools.ipynb
```
 

---

## Contributors

*Provided to you by digi-Borg FinTek*, 
Dana Hayes: nydane1@gmail.com

---

## License

Columbia U. Engineering