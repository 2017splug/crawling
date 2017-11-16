import requests
from bs4 import Beautifulsoup

import urllib2

url="http://www.naver.com"
handle=urllib2.urlopen(url)
data=handle.read()
soup=BeautifulSoup(data)
article=str(soup('div',{'class':'article',}))
print (article.decode('utf-8'))
