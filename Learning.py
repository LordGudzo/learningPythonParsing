# pip install requests
# pip install bs4
import requests

link = "https://it-black.ru/tpost/r04gg7ugn1-chisla-v-python"
responce = requests.get(link).text           #.content - get information in bytes

with open("1.html", "w", encoding="utf-8") as file:  # save responce as html file
    file.write(responce)