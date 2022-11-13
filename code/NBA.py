# librays
import requests
from lxml import etree

# find data
url = 'https://nba.hupu.com/stats/players'

# Disguise the address
headers = {  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35'}

resp = requests.get(url,headers = headers)

# post data
e = etree.HTML(resp.text)
nos = e.xpath('//table[@class="players_table"]//tr//td[1]/text()')
names = e.xpath('//table[@class="players_table"]//tr//td[2]/a/text()')
teams = e.xpath('//table[@class="players_table"]//tr//td[3]/a/text()')
scores = e.xpath('//table[@class="players_table"]//tr//td[4]/text()')

# Organize your data
with open('NBA.txt','w',encoding = 'utf-8 ') as f:
    for no,name,team,score in zip(nos,names,teams,scores):
        f.write(f'排名:{no}姓名:{name} 球队:{team} 得分:{scores}\n')
     