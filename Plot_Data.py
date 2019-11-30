import yfinance as yf
from datetime import datetime
import matplotlib.pyplot as plt
 
def plot_data(STOCK,PRICE):
    # Get the data for the stock by specifying the stock ticker, start date, and end date
    data = yf.download(STOCK,'2016-01-01',datetime.today().strftime('%Y-%m-%d'))
 
    # Plot the close prices
    data.Close.plot()
    plt.axhline(y=120.2, color='r', linestyle='-')
    plt.show()