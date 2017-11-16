import requests
from bs4 import BeautifulSoup

url = 'http://music.bugs.co.kr/chart'

r = requests.get(url)
html_code = r.text
soup = BeautifulSoup(html_code, 'html.parser')
rank_inner = soup.find('table', {'class':'list trackList byChart'})
f = open("./bugs.txt", "w")
for rank, span in enumerate(rank_inner.findAll('p',{'class':'title'})):
#	print("%dwii" % (rank+1)), span.text
	spann = span.text
	f.write(spann.encode('utf-8'))
f.close()
