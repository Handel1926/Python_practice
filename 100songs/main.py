from bs4 import BeautifulSoup
import requests


response = requests.get("https://www.billboard.com/charts/hot-100/1991-04-27/")
site_text = response.text

soup = BeautifulSoup(site_text, "html.parser")
all_music = soup.find_all("span", class_="chart-element__information__song")
music_title = [music.getText().strip("\t\n") for music in all_music]
top_music_titles = music_title[7::4]