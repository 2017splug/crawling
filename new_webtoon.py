#!/usr/bin/env python
#-*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests
import urllib

def get_html(url):
	_html = ""
	resp= requests.get(url)
	if resp.status_code == 200 :
		_html = resp.text
	return _html

def download_image(url, name):
	file_name = name+'.jpg'
	urllib.request.urlretrieve(url, file_name)

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
		
