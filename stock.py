import datetime 
import time
from plyer import notification
import bs4
import requests
from bs4 import BeautifulSoup

def stock():
    urlfb = requests.get("https://finance.yahoo.com/quote/META?p=META")
    urlgoog = requests.get("https://finance.yahoo.com/quote/GOOG?p=GOOG")

    datafb = BeautifulSoup(urlfb.text, "html5lib")
    datagoog = BeautifulSoup(urlgoog.text, "html5lib")

    a = datafb.find_all('div', {'class': "D(ib) Mend(20px)"})[0].find('fin-streamer').text
    print(a)

    notification.notify(
        title = "Facebook".format(datetime.date.today()),
        message = a,
        app_icon = "C:/My Files/Github Project/Jarvis Assistant/stock.ico",
        timeout = 20
    )

