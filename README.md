# PythonTradingScraper

version 1.1
  - Connects to Market watch for a specified ticker and retrieves real time data
  - Checks this realtime data until it reaches a specified target (Script checks it every 60 seconds(can change this))
  - If the price target is hit, sends me an email informing that the price target has been reached

version 1.2
  - Created basic GUI to get ticker from user
  - Will now get price from any valid ticker

version 1.3
  - Connected to IEX api to get list of stocks and store in csv
  
version 1.3.1
  - Reverted back to 1.2 and improved it
  - Fixed bugs to do with invalid Tickers
  - All S&P 500 Stocks are available

version 1.4
  - Added method to pass operators for different types of alerts(greater than, equal etc)
  - Fixed UI for invalid Ticker
  - Added check to see if 'Price' inputed is numerical and greater then 0.0

  Version 2.0 (DATA PLOTTING)
  - Starting to do plotting data
  - Can now get graph of any stock