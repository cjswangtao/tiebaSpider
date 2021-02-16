""" 爬取楼中楼(测试数据用) """
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import Request
import re
import json
from urllib.parse import quote
import  string
import requests

result = []
#4796371684帖子的url
tiezi_url = "https://tieba.baidu.com/p/4796371684"
# 伪装浏览器的请求头
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)'
}
# https://tieba.baidu.com/p/comment?tid=4796371684&pid=98301178347&pn=2
# 
# #

result= {}

#解析url为soup
def getSoup(url):
    agent_url = Request(url=url,headers=headers)
    html = urlopen(agent_url).read().decode("utf-8")
    soup = BeautifulSoup(html,features="lxml")
    return soup

def getUrl(pid,pn):
    return "https://tieba.baidu.com/p/comment?tid=4796371684&pid="+pid+"&pn="+str(pn)
soup = getSoup(tiezi_url)

def iter(elems):
    for elem in elems:
        print(elem)
""" 
98301178347
98311082613
98312370469
98324751499
98326138923
98326344840
98327011652
98327084507
98338563143
98351586782
98377576559
98404269436
98446297600
"""

#根据xhr分析网络通信 获得基础的url组合,在网页源码搜索清洗
elems = soup.find_all("div",{"class":"l_post j_l_post l_post_bright"})
url = getUrl("98404269436",0)
soup = getSoup(url)

#获得最后一页的数字pns
a_pages = soup.find_all("a",{"href":re.compile("#[0-9]")})
if len(a_pages) == 0:
    pns = 2
for a_page in a_pages:
    if a_page.string == "尾页":
        pns = int(a_page["href"].replace("#","")) + 1


for pn in range(1,pns):
    soup = getSoup(getUrl("98404269436",pn))
    span_tages = soup.find_all("span",{"class":"lzl_content_main"})
    for span_tage in span_tages:
        ans = re.sub(r'<\/?.+?\/?>',"",str(span_tage)) #清洗所有的标签
        print(ans)
#添加了
