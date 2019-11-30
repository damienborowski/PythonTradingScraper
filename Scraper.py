import requests
import smtplib
import time
import bs4
import sys
import PySimpleGUI as sg
import pandas as pd
from bs4 import BeautifulSoup
import operator
from Plot_Data import plot_data

# Pull the list of S&P 500 symbols from CSV files
DataBase = pd.read_csv('S&P500-Symbols.csv', index_col=[0])

site_to_scrape = "https://www.marketwatch.com/investing/stock/"
STOCK = ""
PRICE = 0

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}
# Display the main window to the user
def GUI():

    global  site_to_scrape  
    global  STOCK
    global PRICE

    sg.change_look_and_feel('Black')	# Add a touch of color

    # All the stuff inside your window.
    layout = [
            [sg.Text('Enter Ticker',size=(10, 1)), sg.Input(key='Ticker')],
            [sg.Text('Enter Price', size=(10, 1)), sg.Input(key='Price')],
            [sg.Button('Submit')] 
            ]

    # Create the Window
    window = sg.Window('Alert', layout)
    
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, input = window.read()
        if event in (None, 'Cancel'):	# if user closes window or clicks cancel
            break
        if Check_Valid_Ticker(input['Ticker']) == False:
            window.FindElement('Ticker').update('')
            window.FindElement('Price').update('')
            print("INVALID")
        elif Check_Valid_Price(input['Price']) == False:
            window.FindElement('Ticker').update('')
            window.FindElement('Price').update('')
            print("INVALID")
        else:
            print('Ticker: ', input['Ticker'])
            STOCK = input['Ticker']
            PRICE = input['Price']
            print('Alert Price: ',input['Price'])
            site_to_scrape += input['Ticker']
            if event in (None, 'Cancel','Submit'):	# if user closes window or clicks cancel
                break

    window.close()

    # ---- If Ticker is found ---- #
    sg.Popup('Found')

# Check if given stock is in the S&P
def Check_Valid_Ticker(STOCK):
    STOCK = STOCK.upper()
    i = 0
    while i < 505:
        if STOCK == DataBase.values[i]:
            return True
        i += 1
    # ---- If Invalid Ticker ---- #
    sg.Popup('Invalid Ticker')
    return False

# Check if given stock price is valid
def Check_Valid_Price(PRICE):
    try:
        var = float(PRICE)
        if var < 0:
            return False
        return True
    except ValueError:
        return False

# Function for all the different operators
def operators(Alert_price,operator,Stock_price):
    return operator(Alert_price,Stock_price)

# Get the real time price of the stock
def check_price():
    try:
        page = requests.get(site_to_scrape,headers=headers)
    except:
        print("Invalid Ticker")

    soup = BeautifulSoup(page.content, 'html.parser')

    price = soup.find("div",class_="intraday__data").get_text()

    print("=================RESULTS=================")

    Stock_Price = float(price[4:10])
    print('Actual Price: ',Stock_Price)

    #if(Stock_Price > 200):
        #send_mail()

# Send email alert to user
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('borowski.damien1@gmail.com','dxigaueeafstmgum')

    subject = 'Price Target Reached'
    body = ' '

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'borowski.damien1@gmail.com',
        'craven.rafal@gmail.com',
        msg
    )
    print("Email has been sent")

    server.quit
    #sys.exit()

#while(True):
    #check_price()
    #send_mail()
    #time.sleep(1)
#send_mail()
GUI()
print(STOCK)
plot_data(STOCK,PRICE)
#check_price()
#operators(200,operator.gt,150)