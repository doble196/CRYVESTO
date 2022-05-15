# CRYVESTO ANALYSIS: *DIVERSIFYING WITH CRYPTO*

The correlation between stocks and cryptocurrencies has been steadily increasing over the past few years; now both crypto and US equities appear to be moving in tandem. We hypothesize that cryptocurrencies are increasingly becoming exposed to risk factors of the S&P 500. 

Likewise, cryptocurrencies appear to be highly correlated with one another. We hypothesize that the idea of "crypto-diversification” does not exist, or does so minimally.

Collectively, the files of this repo are an investigation of our hypotheses that provides insight as to where cryptocurrency belongs in a portfolio. Our findings inform how to balance cryptocurrency against equities (growth, value) and how to “crypto-diversify” within a portfolio.

**For a summary and conclusion of our findings, please see the "TeamCryvestoPresentation.pdf" document within this repo, pictured here:.**

<img src= "images/analysiscover.png" width="530" height="300">

---
## Technologies

This application leverages python 3.7 with the following packages that require additional installation:

* pandas: an open-source library that offers easy-to-use data analysis tools for Python.
* pathlib: for creation of file paths allowing the application to interact with a computer's filesystem.
* %matplotlib: for creating static, animated, and interactive visualizations in Python.
* statsmodels.api: provides a compliment to scipy for statistical computations including descriptive    
   statistics and estimation and inference for statistical models.
* getFamaFrenchFactors: gets data for Fama French Factors from the Kenneth French library and returns it as a pandas dataframe.
* sklearn: machine learning library featuring various classification, regression and clustering algorithms.
* seaborn: visualization library based on matplotlib providing a high-level interface for drawing attractive and informative     
   statistical graphics.
* yfinance: a Python library that gives you easy access to financial data available on Yahoo Finance.
* hvplot.pandas: a visualization library included in the PyViz package that can produce advanced charts    
  and interactive visualizations. 

---
## Installation Guide

Begin by cloning the GitHub repo (the same repo that this README.md file is contained within) into your terminal. 

Then activate the correct environment by inputting the following command into your terminal:

`conda activate dev`

Within this environment, next install the above listed dependencies. To do so, in your terminal while in this same repo, enter `pip install -r requirements.txt`.

Next, while in your IDE, first open the "cyrvesto_api.ipynb" notebook file and run the code, followed by the remaining notebook files. We suggest running the notebooks corresponding to Parts A, B, and C listed below in sequential order. 

Note: The MCForecastTools library file is included in this repo. Specifically the two notebooks, 20thru21MCs.ipynb and 22MCs.ipynb, use and import the MCSimulation module from the MCForecastTools library.

---

## Usage

The goal of this analysis is to shed insight on how to diversify with cryptocurrency. 

We suggest running the notebooks corresponding to Parts A, B, and C of this analysis in sequential order. Here is the breakdown of each Part:


### **PART A: A BROAD OVERVIEW OF CRYPTO CORRELATIONS**
### cryvesto_analysis.ipynb

* **Section I**: The closing price data is collected for the top 10 cryptocurrencies by market cap for 2016 to present. Closing price data for SPY ETF and QQQ ETF is likewise collected for 2016 to present. Next, the market cap data for the top 10 cryptocurrencies by market cap is collected and plotted in a pie chart.

* **Section II**: Cryptocurrencies are then compared to each other from 2018 to present on measures of volatility, standard deviations, Sharpe ratios, variance, covariance and rolling covariance (calculated in relation to Bitcoin), and beta (likewise calculated in relation to Bitcoin as the index). The volatility, Sharpe ratios, covariance, rolling covaraince, and beta are each plotted.
Next, correlations between cryptos are calculated and plotted for two time periods: 2020-2021 and 2022 year-to-date.

* **Section III**: In the following section, Bitcoin is compared against the S&P 500 and the NASDAQ 100. SPY ETF is used to represent the S&P 500 and QQQ is used to represent the NASDAQ 100. For 2016 to present, Bitcoin's covariance to each index is determined and plotted, along with Bitcoin's beta and rolling beta with each index.
Finally in Section III, Bitcoin's correlation with each SPY and QQQ is determined and plotted for three time periods (2018 thru 2019, 2020 thru 2021, and 2022 year-to-date).


### **PART B: FAMA FRENCH FACTOR REGRESSION ANALYSES**
### BTCFamaFrenchFactors18thru19.ipynb
### BTCFamaFrenchFactors20thru21.ipynb
### BTCFamaFrenchFactors22toP.ipynb

*Note: All three notebooks in this Part (each corresponding to a different time period) have the same sections; all instructions pertain to each.*

Each of these three notebooks in this Part runs a Fama French 4-Factor regression analysis for their respective time period with training and testing of the data. The fourth factor, momentum, is setup to be optional. We chose to examine the Fama French Factors to further understand Bitcoin's expsoure to dimensional market risk, and thereby better assess how to diversify with cryptocurrency.

* **Section I**: Data for Bitcoin and four Fama French Factors (market risk, size, value, and momentum) is collected for respective time period (according to specific notebook) and organized. 

* **Section II**: An OLS regression is performed and expected returns of Bitcoin according to the model are determined.

* **Section III**: The data is trained and tested to determine Bitcoin's excess return on the market that can be explained by the factors.


### **PART C: MONTE CARLO ANALYSES**
### 20thru21MCs.ipynb
### 22MCs.ipynb

*Note: Both notebooks (each corresponding to a different time period) in this Part have the same sections; all instructions pertain to each.*

Both notebooks in this Part run Monte Carlo simulations for (A.) a number of ETFs by themselves, and (B.) the same ETFs paired with Bitcoin in 50/50 weighted portfolios. Please note, the ETF simulations by themselves are to serve as a baseline for comparison when the same ETF is combined with Bitcoin. ETFs were chosen as per our Fama French Factors: size and value (which Bitcoin seems to have exposure to particulary in 2020 and 2021). This part of the analysis expands upon our Fama French Factor findings in Part B, likewise examining Bitcoin's risk-exposure to various aspects of the market so that we can better assess how to diversify with cryptocurrency.

* **Section I**: Collect and organize data for Bitcoin and four ETFs: 
"VOT" (Vanguard Mid-Cap Growth ETF, a midcap growth fund; chose midcap to factor out size), "IWS" (iShares Russell Mid-Cap Value ETF, a midcap value fund; chose midcap to factor out size), "MGC" (Vanguard Mega Cap ETF, a fund with large caps only to feature the large cap end of the size spectrum), and "EWSC" (Invesco S&P SmallCap 600 Equal Weight ETF, a fund with small caps only to feature the small cap end of the size spectrum).

* **Section II**: Run Monte Carlo simulations for each ETF by itself and for each ETF combined with Bitcoin in a 50/50 weighted portfolio.

* **Section III**: Summarize Monte Carlo results.

---

## Contributors

Nicole Roberts, Scott Marler, Ashok Pandey, Rensley Ramos, Dane Hayes

---

## License

[BSD 3](https://choosealicense.com/licenses/bsd-3-clause-clear/): BSD 3-clause is a permissive licence, allowing nearly unlimited freedom with the software as long as BSD copyright and license notice is included.
