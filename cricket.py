import datetime 
import time
from plyer import notification
from bs4 import BeautifulSoup
import requests

def cricket():
	html_text = requests.get('https://sports.ndtv.com/cricket/live-scores').text
	soup = BeautifulSoup(html_text, "html.parser")
	sect = soup.find_all('div', class_='bdy_ovr-wrp')

	section = sect[0]
	description = section.find('span', class_='description').text
	location = section.find('span', class_='location').text
	current = section.find('div', class_='scr_dt-red').text
	link = "https://sports.ndtv.com/" + section.find(
		'a', class_='scr_ful-sbr-txt').get('href')

	try:
		status = section.find_all('div', class_="scr_dt-red")[1].text
		block = section.find_all('div', class_='scr_tm-wrp')
		team1_block = block[0]
		team1_name = team1_block.find('div', class_='scr_tm-nm').text
		team1_score = team1_block.find('span', class_='scr_tm-run').text
		team2_block = block[1]
		team2_name = team2_block.find('div', class_='scr_tm-nm').text
		team2_score = team2_block.find('span', class_='scr_tm-run').text
		print(description)
		print(location)
		print(status)
		print(current)
		print(team1_name.strip())
		print(team1_score.strip())
		print(team2_name.strip())
		print(team2_score.strip())
		notification.notify(
		title = "Cricket".format(datetime.date.today()),
		message = "Location-" +location +"\n"+"Status-" + status +"\n"+"Time-" + current +"\n"+"Team1-" + team1_name.strip() 
		+"\n"+"Team1 Score-" + team1_score.strip() +"\n"+ "Team2-" + team2_name.strip() +"\n" +"Team2 Score-" +  team2_score.strip() ,
		app_icon = "C:/My Files/Github Project/Jarvis Assistant/cricket.ico",
		timeout = 20
	)
	except:
		notification.notify(
		title = "Cricket".format(datetime.date.today()),
		message = "No Live Match at this Time" , 
		app_icon = "C:/My Files/Github Project/Jarvis Assistant/cricket.ico",
		timeout = 10
		)

if __name__ == "__main__":
	cricket()
