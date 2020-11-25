# FinTech Bootcamp University of Toronto
# Can you predict the corn price with weather features

## 1. Summary
The aim of this project is to se see if we can use weather data to predict the US corn price. The price of corn is a complex macro-economic 
Various datasets were extracted and analyzed,  visualizations done in Pyviz, Time series analysis performed to predict the future price of corn, which was then used in a XG Boost Machine learning model. The outcome was then used validate our research and assumptions.

xxx

## 2. Background

Maize (corn) is the dominant grain grown in the world. Total maize production in 2018 equaled 1.12 billion tons. Maize is used primarily as an animal feed in the production of eggs, dairy, pork and chicken. The US produces 32% of the world’s maize followed by China at 22% and Brazil at 9%. In addition, the US is the leading consumer of corn worldwide. In 2019/2020, the U.S. consumed about 12.3 billion bushels of corn. China, the runner up, consumed about 10.98 billion bushels of corn in that year. </br>

Corn Futures are traded at the Chicago Board of Trade (CBOT), NYSE Euronext (Euronext) and Tokyo Grain Exchange (TGE). Commodities are traded based on margin, and the margin changes based on market volatility and the current face value of the contract.

### What determines the price of corn?
In a free market economy, price is determined by the supply and demand for a product or commodity. Short-term price gyrations often occur and can be influenced by market reactions to news concerning such things as weather, government reports and/or policy. Corn is a commodity that reflects this scenario.</br>

  #### Supply sources:
  1. Leftover stocks from previous year
  2. Domestic production </br>
        Weather plays a critical role in domestic production - especially for planting and harvesting dates which impact the size of the crop. The United States Department of Agriculture (USDA) publishes several crop reports each year, which often cause wide price swings as the market interprets the numbers.
  3. International imports

  #### Demand sources: 
  1. Feed and residual
  2. Exports - US is a major supplier of corn to various countries
  3. Food and industrial use is at approximately 40% of the supply, of which the largest component is ethanol production. 

  #### Price: Supply vs Demand
  Supply and demand interact to determine price. The market does react to short-term events, but knowing the sources of supply and demand, and when estimates of these are released, will provide the opportunity to purchase corn and cattle feed at lower prices.


#### Corn price fluctuation: 
* Seasonal tendency of corn price:
   * Late June or early July - corn hits yearly peak prices
   * November - harvest time - corn hits yearly lowest price
   * November - March during winter, corn prices has least volatility.

* Ideal weather conditions:
In 


## 2. Project Approach 

|Phase | Description | Summary of Findings |
| --- | --- | --- |
| **Phase 1: Research** | 4 Commodities were reasearched to determine which would be suitable for project: Corn, Soy, Cocoa and Sugar | Limit scope to corn due to the use and production in US, limiting data extraction to only US |
| **Phase 2: Data extraction** |Datasets were extracted from Jan 2000 to Nov 2020: Corn price, Corn futures, weather max min and precipitation from 51 states, ethanol futures, USD index, USD Inflation | Reviewed the size of data and elimitate|
| **Phase 3: Scope refinement and data imports** | Data timeframe was from Jan 2005 to Nov 2020: Corn price, weather max min and precipitation from 5 states in corn-belt, ethanol futures, USD index, USD Inflation | Data imported into Jupyter notebooks for data cleanup and analysis
| **Phase 4: Weather data analysis** |   |   |
| **Phase 5: Time series analysis of corn price** |   |   |
| **Phase 6: Algorythmic Trading of corn price** | Constructed a comprehensive trading template fetching data to trading performance evaluation dashboard of corn  |   |
| **Phase 7: Machine learning for validation of assumptions** 
| **Phase 8: Overall Findings and conclusion** | All fidings from various phases were evaluated and compared  | Conclusion formulated  |

## 3. Data
The following table summarizes the data files used, their links and where the data was extracted from:

|Data | Description | Source | Link |
| --- | --- | --- | --- | --- |
| Corn price | Daily price of corn   | www.Macrontrends.net  | [Corn Price](./Resources/corn-prices-historical-chart-data.csv)   |
| Corn futures | Corn futures traded in commodity exchange   | www.barchart.com    |  [Corn Futures](./Resources/corn_)  |
| Ethanol futures  |    |     |    |
| USD Index  |    |     |    |
|   |    |     |    |
|   |    |     |    |
| Weather data  |  5 states - min, max and precipitation  |  NOAA   |  [Weather data](./Resources/corn_belt_weather.csv) |

[Corn Actual vs Forecasted Price](./Resources/TS_Corn_Actual_Forecasted.png)

## 4. Weather information
Weather Data for the states Illinois, Indiana, Nebraska, Ohio, Iowa was pulled from the [NOAA's National Centers for Environmental Information (NCEI) Climate Data Online](https://www.ncdc.noaa.gov/cdo-web/webservices/v2) from January 1, 2000 to December 31, 2019. 

Ten weather stations from each state were chosen at random to provide daily data on max temperature (TMAX), min temperature (TMIN), and precipitation (PRCP). The weather stations inside each state were averaged to provide one dataset (TMAX, TMIN, PRCP) per day.
![map](./Images/map.png)


## 4. Time series analysis
The ARIMA time series analysis was performed with and without seasonality. 

### ARIMA time series analysis findings without seasonality
   * Training and validation datasplit was done at 70%/30% and Hodrick-Prescott Filter was used to decompose the data into trend and noise
   * Autocorrelation and partial autocorrelation analysis was performed to determine lag to be applied in ARIMA model
   * Corn returns was forecasted using ARIMA model using order of 3,1,2. 
   * Forecasted value was then calculated from the adjusted closing price ?????
      ![Corn Actual vs Forecasted Price](./Images/TS_Corn_Actual_Forecasted.png)

### ARIMA time series analysis findings with seasonality
   * 

_____________________


## 5. Algorithmic Trading

The algorithmic trading was performed on forecasted U.S. corn price solely in 2020. Both the portfolio performance for backtesting and the actual trading performance were evaluated and presented in a dashboard.

* Forecased Corn Price: The corn price for 2020 Jan - 2020 Mar was predicted using linear regression

![future_corn_price.png](./Images/future_corn_price.png)

* Technical Indicator: Crossover between 10-day simple moving average (SMA10) and 30-day simple moving average (SMA30)

* Signals: Buy when `SMA10 < SMA30`; sell when `SMA10 > SMA30`; hold when `SMA10 = SMA30`

* Trading Performance Evaluation:  
  - Shares on Hold: `27132`
  - Account Balance: `$0.295`
  - Account Total Monetary Value: `$103968.4`
  - Account Initial Capital: `$100000`

Trading Activities Recorded </br>
![trading_dashboard.png](./Images/trading_dashboard.png)

*  Portfolio Performance Evaluation from backtesting:
  - Annual Return: `0.21%`
  - Cumulative Return: `0.072%`
  - Annual Volatility: `0.319%`
  - Sharpe Ratio: `0.645`
  - Sortino Ratio: `0.971`

Commodity Portfolio Performance Evaluation </br>
![portfolio_dashboard](./Images/portfolio_dashboard.png)

Forecasted Corn Price Chart with trading signals labeled </br>
![portfolio_eval](./Images/portfolio_eval.png)


## 6. Deep Learning: XG Boost

The XGBoost model was used to evaluate our initial understanding of factors that impact the corn prices. Specifically, the corn price prediction and the associated performance evaluation was performed with solely 
weather data and with all features, respectively.

### XGBoost Modelling with weather data alone

- Features used:  `avg_prcp`, `avg_max` and  `avg_min` 
- Data Range: `2005 - 2020`
- window of size 5 was used 
- 70-30 train-test split
- Median Average Error (MAE): `0.722`
- Average Evaluation Score: `0.703`

![xgboost_weather_data](./Images/xgboost_weather_data.png)


### XGBoost Modelling with all features

- Features used: `avg_prcp`, `avg_max`, `avg_min`, `USD_index`, `ethanol_future`, `natural_gas_future`
- Data Range: `2005 - 2020`
- window of size 5 was used 
- 70-30 train-test split
- Median Average Error (MAE): `0.133`
- Average Evaluation Score: `0.187`

![xgboost_all_data](./Images/xgboost_all_data.png)


## 7. Major Findings


