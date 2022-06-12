<h1 style="text-align:center">Predicting BTC Closing Value Based on Past 30 days of Data </h1>
<h5 style="text-align:center"> Mike Limpus, Michael Hackett, Katie Vickstrom, Josh Hansen </h5>

## Introduction
Given the volatility of the crypto market lately, we are interested in seeing if we can predict Bitcoin prices based on the historical and recent history of Bitcoin prices. We want to predict tomorrow's closing price based on the past 30 days closing prices.

## Choice of dataset:
We downloaded a csv from https://www.investing.com/crypto/bitcoin/historical-data where chose the timeframe of Bitcoin historical data from 6/4/2020-6/4/2022. This was then uploaded to Github as there is no direct link. <a href='https://raw.githubusercontent.com/KatherineVickstrom/DataScience/main/Bitcoin_Historical%20Data_%20Investing_com_20200604_20220604.csv'> (Link to GitHub)</a>  <br>
It is important to note that our chosen data set represents prices at a single point in time during the day. A more in-depth look could use data by the second, but this is out of the scope of our experiments.
### Target to predict: 
'Price' - the closing price of Bitcoin at the end of each day. 