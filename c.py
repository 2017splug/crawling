import requests
from bs4 import BeautifulSoup


response=requests.get('https://comic.naver.com/index.nhn?titleId=20853&weekday=tue')

html=response.text

soup=BeautifulSoup(html,'html.parser')

for tag in soup.select('li[class=rank01]'):
	print(tag.text)
