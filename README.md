# CRYVESTO Application - Smart Way to Build a Portfolio

This application allows a user to build a portfolio by selecting upto 2 Cryptos and upto 3 ETFs from the lists provided. The user gets to assign weightage to each Crypto and ETF in the portfoilio.

It then does a four factor analysis on the Cryptos, followed by Sharpe Ratios and Betas against the ETFs selected. And, finally does a Montecarlo simulation projecting the returns on the portfolio constructed.

## User Story
Given the hype and excitement of Cryptocurrencies, a lot of people have made loads of money and a lot have lost their shirt.  We believe there is a need to figure out a smart way to buy Cryptos.  Founders of our startup have chartered the team to develop a prototype of the application that can smartly build a portfolio incorporating Cryptos. Specifically, the portfolio should allow for selection of upto 2 Cryptos and upto 3 ETFs; allow flexibility to assign weightage to the selected Cryptos and ETFs, enabling the user to obtain a desired projected performance.

---

## Acceptance Criteria  
The application must meet the following acceptance criteria:  

### Selecting Cryptos  

* From a selection of Cryptos, the user should be able to select upto 2 Cryptos
* If the user tries to enter more than 2 Cryptos, guide him accordingly
* Should allow for smooth exit at this level
* Inform the user of the Crypto behavior whether it is in line with the Market, or behaving like a Value or Growth Stock, by running Famma French analyisis on the selected Crypto.


### Selecting ETFs  

* From a selection of ETFs, the user should be able to select upto 3 ETFs
* If the user tries to enter more than 3 ETFs, guide him accordingly
* Should allow for smooth exit at this level
* Inform the user of:
    - the risk adjusted returns of the selected Crypto
    - Betas of the Crypto against the selected ETFs
* The user should be allowed to make changes to his selection at this point.

### Assigning Weights and Portfolio Performance Projection

* The user should be able to assign weights to the selected Cryptos and ETFs. Sum of all the weights should equal 1.
* The user should be given an option to change the number of years (2 - 5) of historical data to base the performance on. 
* To calculate number of years of projection, divide number of years of historical data by 2 (use integer division).
* Run MonteCarlo simulation on the portfolio and display the projected performance indicating
    - Number of years of historical data
    - $10,000 as the sample value of Portfolio
    - Display the weightage and dollar amounts of Cryptos and ETFs selected
    - Display the number of years for the performance projection
    - Display the projected portfolio performance based upon 95% CI values of the simulation results
* The user is allowed an option to repeat the above steps with different allocation percentages and number of years of historical data.

---

## The CRYVESTO App 

The application uses the following Cryptos and ETFs: 
- Tickers used ={'BTC-USD': 'Bitcoin',
                'ETH-USD': 'Ethereum',
                'BNB-USD': 'Binance Coin',
                'SOL-USD': 'Solana',
                'AVAX-USD': 'Avalanche',
                'DOT-USD': 'Polkadot',
                'DOGE-USD': 'Dogecoin'}
- ETFs used ={'SPY': 'S&P 500  ',
                'IYW':'iShares U.S. Technology',
                'QQQ': 'Nasdaq 100     ',
                'RYT': 'Invesco S&P 500 Equal Weight Technology',
                'IETC': 'iShares Evolved U.S. Technology',
                'IWM': 'iShares Russell 2000',
                'BND': 'Vanguard Total Bond Market',
                'ARKK': 'Ark Innovation',
                'RPV': 'Invesco S&P500 Pure Value'}


### Selecting Cryptos  
    
* The user is prompted to select a maximum of 2 cryptos from the displayed list of Crypto, listed above.
* The user is given an option to exit at this point.
* After the selection, **ffanalyse** function (stored in our custom fourfactor library, fourfacator.py)is called to do a Famma French Four Factor analysis. Using the resulting betas, the user is informed as follows:(beta_s, beta_v, beta_m are beta-SMB, beta-HML, and beta-Mkt respectively. {tkr} being the selcted Crypto)
    - if beta_s > beta_v and beta_s > beta_m, then display
        - Based upon Famma French, {tkr} is behaving more like a Growth stock, you may want to balance your Portfolio using some Value and Broader Market elements
    - if beta_v > beta_s and beta_v > beta_m, then display
        - Based upon Famma French, {tkr} is behaving more like a Value stock, you may want to balance your Portfolio using some Growth and Broader Market elements
    - if beta_m > beta_v and beta_m > beta_s, then display
       - Based upon Famma French, {tkr} is behaving more in line with Market than other factors, you may want to add Value and Growth stocks
       
### Selecting ETFs  

* The user is prompted to select a maximum of 3 ETFs from the displayed list of ETFs, listed above.
* The user is given an option to exit at this point.
* The app calls **do_risk_return_analysis** function (from our custom library, xactcryptos.py). For each Crypto selected, it performs the following:
    - gets the historical data for 3 years from yahoo finance using **get_data** from the same library
    - gets the Sharpe ratios using **get_sharpe**
    - gets the betas against each ETF using **get_beta** 
    - displays the Sharpe and Betas
* The user is asked again if s/he wants to change the ETF selection based upon the results of the previous selection

### Assigning Weights and Portfolio Performance Projection

*  the user is asked to assign weights to the selected Cryptos and ETFs. The sum of weights should be 1 and is validated. Reprompt if necessary
* the user is asked for the number of years of historical data to use for the simulation. At present s/he can select from 2-5 years, 3 being the default.
* call **run_montecarlo** function (from our library, MC_simulation.py):
    - runs the MonteCarlo simulation
    - displays the results of the simulation
        - Number of years of historical data
        - $10,000 as the initial investment value of the Portfolio
        - weightage and dollar amounts invested for the selected Cryptos and ETFs
        - number of years for the performance projection
        - projected portfolio performance based upon 95% CI values of the simulation results
* The user is asked to repeat the above steps with different allocation percentages and number of years of historical data.


---

## Technologies
The application is developed using:  
* Language: Python 3.7,   
* Packages/Libraries: Pandas, os, Alpaca SDK, Resources, json, MCForecastTools for MCSimulation, matplotlib, yfinance
* Development Environment: VS Code and Terminal, Anaconda 2.1.1 with conda 4.11.0, Jupyterlab 3.2.9  
* OS: Mac OS 12.1

---
## Installation Guide
Following are the instructions to install the application from its Github respository.  

### Clone the application code from Github as follows:
* copy the URL link of the application from its Github repository     
* open the Terminal window and clone as follows:

    1. %cd to_your_preferred_directory_where_you want_to_store_this_application  
    2. %git clone URL_link_that_was_copied_in_step_1_above   
    3. %ls       
      Project-1   
    4. %cd Project-1     

At this point you will have the the entire application files in the current directory as follows:

* README.md - this file that you are reading
* cryvesto.py  - the main program for the app
* fourfactor.py - the Famm French Four Factor analysis custom library
* xactcryptos.py - the library of functions used for getting data, sharpe-ratios, betas etc
* MC_simulation.py - the library with functions to run the MonteCarlo simulation
* MCForecastTools.py - MonteCarlo simulation library

---

## Usage
The following details the instructions on how to run the application.  

### Setup the environment to run the application
Setup the environment using conda as follows:  

    5. %conda create dev -python=3.7 anaconda  
    6. %conda activate dev  
### Run the Application
The code requires myapi.env, which is there. you may change it to your ALPACA API keys. It is currently set to my API keys, which might work for now. 
    
    7. %python cryvesto.py

---

**NOTE**:
* Your prompt will look something like (dev) ashokpandey@Ashoks-MBP Project-1 %,  with:  
    - "(dev)" indicating the activated "dev" environment,   
    - ' ashokpandey@Ashoks-MBP ' will be different for you as per your environment, and   
    - 'Project-1' directory is where cryvesto.py is located.  
    - '%' sign is the shell prompt, it could be a $ sign on your machine  

---

## Contributors
Ashok Pandey - ashok.pragati@gmail.com, www.linkedin.com/in/ashok-pandey-a7201237  
Nicole Roberts - elle.nicole.roberts@gmail.com, www.linkedin.com/in/nicolerobertsdesigner/
Dane Hayes - nydane1@gmail.com
Scott Marler - scottjmarler@gmail.com, https://www.linkedin.com/in/scott-marler-212040b6/
Rensley Ramos - ranly196@gmail.com, www.linkedin.com/in/rensley-2-nfty

---

## License
The source code is the property of the developer. The users can copy and use the code freely but the developer is not responsible for any liability arising out of the code and its derivatives.

---

