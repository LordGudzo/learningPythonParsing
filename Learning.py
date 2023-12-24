# pip install requests    - for requests))
# pip install bs4         - for parsing
# pip install fake-useragent   - for changes user-agent

import requests
from bs4 import BeautifulSoup
import fake_useragent

user = fake_useragent.UserAgent().random
header = { 'User-Agent': user}


link = "https://wtools.io/ru/check-my-user-agent"
responce = requests.get(link, headers = header).text           #.content - get information in bytes

#   with open("1.html", "w", encoding="utf-8") as file:  #save responce as html file
#      file.write(responce)

soup = BeautifulSoup(responce, "lxml")
user_Agent = soup.find('pre', id = "resultInputpre").text

print(f"You user Agent: {user_Agent}")