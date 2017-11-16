import requests
from bs4 import BeautifulSoup

url = 'http://www.ssu.ac.kr/web/kor/edu_b_01'

r = requests.get(url)
html_code = r.text
soup=BeautifulSoup(html_code,'html.parser')
rank_inner = soup.find('ul',{'class':'reset'})
f = open("./jy.txt",'w')
for rank,span in enumerate(rank_inner.findAll('a',{'class':'text'})):
	print(span.text)
f.close()
