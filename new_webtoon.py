#!/usr/bin/env python
#-*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests
import urllib
import os
import shutil
import datetime

def get_html(url):
	_html = ""
	resp= requests.get(url)
	if resp.status_code == 200 :
		_html = resp.text
	return _html

def download_image(url, name):
	dirname = '../webtoon'
	if not os.path.isdir('../webtoon'):
		os.mkdir('../webtoon')
	file_name = name+'.jpg'
	urllib.request.urlretrieve(url, file_name);
	today = datetime.date.today()

	targetpath = "../webtoon/" + today.isoformat()
	for file in os.listdir(os.getcwd()):
		if file.endswith(".jpg"):
			if not os.path.isdir(targetpath):
				os.mkdir(targetpath)
				shutil.move(file, targetpath)
			else:
				shutil.move(file, targetpath)
	print("webtoon폴더로 업데이트 된 네이버 웹툰 Thumbnail 가져옴")


def find_new_webtoon():
	URL = "http://comic.naver.com/webtoon/weekday.nhn"
	source_code=get_html(URL)
	soup=BeautifulSoup(source_code, "lxml")
	name = soup.find("div", {"class":"webtoon_spot2"}).find("ul")
	num = 1

	for keywords in name.findAll("div",{"class":"thumb7"}):
		srcurl = keywords.a.img.get('src')
		name = keywords.a.img.get('alt')
		download_image(srcurl, name)

find_new_webtoon()
