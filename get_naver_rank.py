import requests
import os
import shutil
from bs4 import BeautifulSoup

def get_rank():
	response = requests.get('http://datalab.naver.com/keyword/realtimeList.naver?where=main')
	dom = BeautifulSoup(response.text, 'html.parser')
	result = dom.find_all('ul')
	f = open("./naver_rank.txt", "w")
	for res in result:
		if res['class'][0] == 'rank_list':
			keywords = res.find_all('span')
			for key in keywords:
				f.write(key.contents[0]+"\n")
			break

	f.close()
	
	dirname = 'naver_rank'
	if not os.path.isdir('naver_rank'):
		os.mkdir('naver_rank')

	for file_list22 in os.listdir('../test/naver_rank'):
		if os.path.exists('naver_rank.txt'):
			os.remove('naver_rank.txt')

	for file_list in os.listdir('../test'): 
		if os.path.exists('naver_rank.txt'):
			shutil.move('naver_rank.txt', '../test/naver_rank')

get_rank()

