import requests
import smtplib
import time
import bs4
import sys
import PySimpleGUI as sg
from bs4 import BeautifulSoup

site_to_scrape = "https://www.marketwatch.com/investing/stock/"

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}

def GUI():

    global  site_to_scrape  

    # ------ Menu Definition ------ #
    menu_def = [['&Tickers',['AAPL','AMZN','MSFT']]]

    sg.change_look_and_feel('Black')	# Add a touch of color

    # All the stuff inside your window.
    layout = [[sg.Menu(menu_def)],[sg.Text('Enter ticker'), sg.InputText()],
            [sg.Button('Search')] ]

    # Create the Window
    window = sg.Window('TradesMan', layout)
    
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, ticker = window.read()
        if event in (None, 'Cancel'):	# if user closes window or clicks cancel
            break
        if len(ticker[0]) <= 4:
            print('You entered ', ticker[0])
            site_to_scrape += ticker[0]
            print(site_to_scrape)

    window.close()

def check_price():
    try:
        page = requests.get(site_to_scrape,headers=headers)
    except:
        print("Invalid Ticker")

    soup = BeautifulSoup(page.content, 'html.parser')

    price = soup.find("div",class_="intraday__data").get_text()

    print("=================RESULTS=================")

    converted_price = float(price[4:10])
    print(converted_price)

    #if(converted_price > 200):
        #send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('borowski.damien1@gmail.com','dxigaueeafstmgum')

    subject = 'Price fell down'
    body = 'TESTING'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'borowski.damien1@gmail.com',
        'neimadb@hotmail.com',
        msg
    )
    print("Email has been sent")

    server.quit
    sys.exit()

#while(True):
    #check_price()
    #time.sleep(60)

GUI()
check_price()

