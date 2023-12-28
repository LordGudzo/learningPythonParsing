import requests
from bs4 import BeautifulSoup
import fake_useragent
from password import login_password

session = requests.Session()  # storages cookies
user = fake_useragent.UserAgent().random
header = { 'User-Agent': user}

#block auth

data = {                    #need find in network in dewtools (post)
    'post_data': f"username={login_password['login']}&password={login_password['password']}&remember_me=on&act=login"
}


link_auth = "https://zastavok.net/includes/ajax/auth.php"
responce_auth = session.post(link_auth, data=data, headers=header)



cookies_dict = [        #rewrites cookies
    {'domain': key.domain, 'name': key.name, 'path': key.path, 'value': key.value}
    for key in session.cookies
]

session2 = requests.Session()
for cookies in cookies_dict:
    session2.cookies.set(**cookies) 

# work with user setting profile
link_user_setting = "https://zastavok.net/user/LordGudzo/settings/"
responce_user = session.get(link_user_setting, headers=header).text
soup = BeautifulSoup(responce_user, "lxml")
settings_block = soup.find("div", id="subscr")
user_login = settings_block.find("div", class_="c2").text
print(user_login)