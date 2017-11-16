def get_html(url):
	_html=""
	resp=requests.get(url)
	if resp.status_code == 200:
		_html=resp.text
	return _html
from bs4 import BeautifulSoup
	URL="http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=tue&page=1"
html=get_html(URL)
soup = BeautifulSoup(html,'html.parser')
webtoon_area=soup.find("table",{"class": "viewList"}) .find_all("td", {"class":"title"})
def insert_webtoon_info(simple_redis, infos):
	for info in infos:
		res=simple_redis.redis_hash_set("maso",info[0],info)
<div clas="thumb">
	<a href="/webtoon/list.nhn?titleld=183559&weekday=mon"
	onclick="clicker(this,'tgn*m.img','','1',event)">
	<img onerror="this.src='http://static.comicmmon/blank.gif'"
		src="http://thumb.comic.naver.net/webtoon/t83x90.jpg"
		width="83" height="90" title="top of god" alt="top of god">
	<span class="mask"></span>
	</a>
</div>

