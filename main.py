import requests
from bs4 import BeautifulSoup
from time import sleep



headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'pl,en-US;q=0.7,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate',
    'Origin': 'http://booksclub.pl',
    'Connection': 'keep-alive',
    'Referer': 'http://booksclub.pl/',
    # 'Cookie': 'bblastvisit=1675683141; bblastactivity=0; bbsessionhash=63a5ebd5bb0f4057cee2a44d5cd06c0a',
    'Upgrade-Insecure-Requests': '1',
}

params = {
    'do': 'login',
}

data = {
    'vb_login_username': 'scumbagbear',
    'vb_login_password': 'BearimusPr1me',
    's': '',
    'securitytoken': 'guest',
    'do': 'login',
    'vb_login_md5password': '15fa375bc349485e30387247198ca8d5',
    'vb_login_md5password_utf': '15fa375bc349485e30387247198ca8d5',
}
linki = ['http://booksclub.pl/showthread.php?t=52673','http://booksclub.pl/showthread.php?t=52674','http://booksclub.pl/showthread.php?t=52672','http://booksclub.pl/showthread.php?t=52670']
with requests.session() as s:
    r = s.post('http://booksclub.pl/login.php', params=params, headers=headers, data=data)
    for i in linki:
        r2 = s.get(i,params=params, headers=headers,data=data)
        soup = BeautifulSoup(r2.text,'html.parser')
        print(soup.find('pre', class_ = 'alt2').text)
        sleep(90)


