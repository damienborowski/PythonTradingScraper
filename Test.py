import pandas as pd
from iexfinance.stocks import Stock
from datetime import datetime
import matplotlib.pyplot as plt
from iexfinance.stocks import get_historical_data

PUBLIC_TOKEN = "pk_221e246c68a6428cbc5f56b47c027a10"
START = datetime(2016, 1, 1)
END = datetime(2019, 7, 30)
STOCK = "MMM"

# Pull the list of S&P 500 symbols from CSV files
DataBase = pd.read_csv('S&P500-Symbols.csv', index_col=[0])
print(DataBase)

def getCompanyInfo(symbols):
    stock_batch = Stock(symbols,token=PUBLIC_TOKEN)
    company_info = stock_batch.get_company()
    return company_info

def getHistoricalPrices(stock):
    return get_historical_data(stock, START, END,output_format='pandas',token=PUBLIC_TOKEN)

sp_company_info = getCompanyInfo(DataBase["Symbol"][:5].tolist())
#print(sp_company_info)

company_info_to_df = []

for company in sp_company_info:
    company_info_to_df.append(sp_company_info[company])

single_stock = getHistoricalPrices(STOCK)
single_stock['close'].plot(label="3M Close")

#plt.title(STOCK)
#plt.show()