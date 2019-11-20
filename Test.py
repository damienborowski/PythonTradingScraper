import pandas as pd
from iexfinance.stocks import Stock
from datetime import datetime
import matplotlib.pyplot as plt
from iexfinance.stocks import get_historical_data

PUBLIC_TOKEN = "pk_221e246c68a6428cbc5f56b47c027a10"

# Pull the list of S&P 500 symbols from CSV files
sp = pd.read_csv('S&P500-Symbols.csv', index_col=[0])

def getCompanyInfo(symbols):
    stock_batch = Stock(symbols,token=PUBLIC_TOKEN)
    company_info = stock_batch.get_company()
    return company_info

def getEarnings(symbol):
    stock_batch = Stock(symbol,token=PUBLIC_TOKEN)
    earnings = stock_batch.get_earnings(last=4)
    return earnings
def getHistoricalPrices(stock):
    return get_historical_data(stock, start, end,output_format='pandas',token=PUBLIC_TOKEN)

sp_company_info = getCompanyInfo(sp["Symbol"][:5].tolist())

company_info_to_df = []
for company in sp_company_info:
    company_info_to_df.append(sp_company_info[company])
columns = ['symbol', 'companyName', 'exchange',
           'industry', 'website', 'CEO', 'sector']
df = pd.DataFrame(company_info_to_df, columns=columns )
df.head()
single_stock_earnings = getEarnings(sp["Symbol"][0])
df_earnings = pd.DataFrame(single_stock_earnings)
df_earnings.head()
start = datetime(2016, 1, 1)
end = datetime(2019, 7, 30)
single_stock_history = getHistoricalPrices(sp["Symbol"][0])
single_stock_history['close'].plot(label="3M Close")
