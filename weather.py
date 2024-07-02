import datetime 
import time
from plyer import notification
import requests
from bs4 import BeautifulSoup
def weather_report(city):
    try:
        url = "https://www.google.com/search?q=" + "weather" + city

        html = requests.get(url).content

        soup =  BeautifulSoup(html, 'html.parser')

        temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd' } ).text

        time_skyDescription = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd' } ).text

        data = time_skyDescription.split('\n')
        time = data[0]
        sky = data[1]

        listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd' } )

        strd = listdiv[5].text

        post = strd.find('Wind')


        print("Temperature is", temp)
        print("Time : ", time)
        print("Sky Description: ", sky)


        notification.notify(
            title = city.capitalize().format(datetime.date.today()),
            message = "Temperature-" +temp +"\n"+"Time-" + time +"\n"+"Sky Description-" + sky ,
            app_icon = "C:/My Files/Github Project/Jarvis Assistant/weather.ico",
            timeout = 20
        )
    except Exception as e:
        notification.notify(
            title = city.capitalize().format(datetime.date.today()),
            message = "For this city information currently not available" ,
            app_icon = "C:/My Files/Github Project/Jarvis Assistant/weather.ico",
            timeout = 5
        )


if __name__== "__main__":
    city = str(input("Enter city name: "))
    weather_report(city)