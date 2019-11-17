import requests
import smtplib
import time
import bs4
import sys
from bs4 import BeautifulSoup

URL = 'https://www.marketwatch.com/investing/stock/aapl'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}

def check_price():
    page = requests.get(URL,headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    price = soup.find("div",class_="intraday__data").get_text()

    print("=================RESULTS=================")

    converted_price = float(price[4:10])
    print(converted_price)

    if(converted_price > 200):
        send_mail()

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

while(True):
    check_price()
    time.sleep(60)