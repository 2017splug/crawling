import requests
import os
import shutil
from bs4 import BeautifulSoup

def get_rank():
	response = requests.get('http://datalab.naver.com/keyword/realtimeList.naver?where=main')
	dom = BeautifulSoup(response.text, 'html.parser')
	result = dom.find_all('ul')
#	URL = "http://datalab.naver.com/keyword/realtimeList.naver?where=main"
#	source_code = get_html(URL)
#	soup = BeautifulSoup(source_code, "lxml")

	f = open("./naver_rank.txt", "w")
	for res in result:
		if res['class'][0] == 'rank_list':
			keywords = res.find_all('span')
			for key in keywords:
				print(key.contents[0]+"\n")
				f.write(key.contents[0]+"\n")
			break

	f.close()
	
	dirname = 'naver_rank'
	if not os.path.isdir('../naver_rank'):
		os.makedirs('../naver_rank')

	for file_list22 in os.listdir('../naver_rank'):
		if os.path.exists('naver_rank.txt'):
			print("exist..")
			os.remove("../naver_rank/naver_rank.txt")

	for file_list in os.listdir(os.getcwd()): 
		if os.path.exists('naver_rank.txt'):
			print("exist..2")
			shutil.move('./naver_rank.txt', '../naver_rank')

	print("naver_rank폴더로 네이버 실시간 검색어  가져옴")

get_rank()

