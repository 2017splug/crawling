#!/usr/bin/env python
#-*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests
import os
import shutil
def get_html(url):
	_html = ""
	resp= requests.get(url)
	if resp.status_code == 200 :
		_html = resp.text
	return _html

def find_title():
	URL = "http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=tue&page=1"
	source_code=get_html(URL)
	soup=BeautifulSoup(source_code, "lxml")

	name = soup.find("table", {"class":"viewList"})

	f = open("./webtoon.txt", "w")
	for keywords in name.findAll("td",{"class":"title"}):
	#	print(keywords.a.text)
		webname = str(keywords.a.text)
		f.write(webname+"\n")

	f.close()

	dirname = 'webtoon_name'
	if not os.path.isdir('webtoon_name'):
		os.mkdir('webtoon_name')

	for file_list2 in os.listdir('../test/webtoon_name'):
		if os.path.exists('webtoon.txt'):
			os.remove('webtoon.txt')


	for file_list in os.listdir('../test'):
		if os.path.exists('webtoon.txt'):
			shutil.move('webtoon.txt', '../test/webtoon_name')
	
find_title()

