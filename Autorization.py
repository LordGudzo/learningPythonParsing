import requests
from bs4 import BeautifulSoup
import fake_useragent
from password import login_password

session = requests.Session()  # storages cookies
user = fake_useragent.UserAgent().random
header = { 'User-Agent': user}

#block auth

data = {                    #need find in network in dewtools (post)
    'username':	login_password['login'],
    'password':	login_password['password'],
    'csrfmiddlewaretoken':	"Di5Mr9zwu4XneLHE9tYzWddVz5COBdUX1o3qf2wjKdt8T3D7eYtCAxoX1TL6Tx7j",
    'mode':	"login"
}


link_auth = "https://dou.ua/ajax-login/"
responce_auth = session.post(link_auth, data=data, headers=header)


cookies_dict = [        #rewrites cookies
    {'domain': key.domain, 'name': key.name, 'path': key.path, 'value': key.value}
    for key in session.cookies
]

session2 = requests.Session()
for cookies in cookies_dict:
    session2.cookies.set(**cookies) 