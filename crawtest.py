import requests
from bs4 import BeautifulSoup

def get_rank():
	response = requests.get('http://datalab.naver.com/keyword/realtimeList.naver?where=main')
	dom = BeautifulSoup(response.text, 'html.parser')
	result = dom.find_all('ul')
	f = open("./rank.txt", "w")
	for res in result:
		if res['class'][0] == 'rank_list':
			keywords = res.find_all('span')
			for key in keywords:
				print(key.contents[0])
				f.write(key.contents[0]+"\n")
			break

	f.close()
		
#f = open("./rank.txt", "w")
#for keywords in name.findAll("td",{"class":"title"}):
#	print(keywords.a.text)
#	webname = str(keywords.a.text)
#	f.write(webname+"\n")
#f.close()

