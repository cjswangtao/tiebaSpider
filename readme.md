<h2>贴吧爬虫</h2>

```
背景：小白放假在家没事，想爬取南京信息职业技术学院贴吧用户关注的贴吧因此写来的项目
不足：贴吧有防爬虫机制(应该是发现ip大量的刷新页面需要验证)，因为是小白入门所以没有解决这个问题
      我当时用无线网来爬取信息的,无法使用的时候换了手机的热点(百度安全验证无法识别手机的网)
优点：本项目的几个python文件是互相独立的，降低零基础学习爬虫的门栏。test文件夹是为了实现思路而写的测试文件
      使用了多线程来加速爬虫(爬个几万条数据还是挺快的)
```
<h4>实现的思路大致如下:</h4>
<p>1.保存南京信息职业技术学院吧的网址</p>
<p>2.根据排名第二精品贴分析，获取层主的全部url</p>
<p>3.根据个人主页来获取关注的贴吧</p>
<p>4.楼中楼通过xhr分析</p>

<h4>运行环境</h4>

```
    网络:手机热点(百度安全验证无法识别的网络)
    数据库mysql 5 + 

```

<h4>运行方式：</h4>

```
   1.安装python环境并配置环境变量
   2.pip3 install beautifulsoup4
   3.pip3 install lxml
   ...
   注意:先运行tiezi.py 再 user.py 再 user_bar.py(测试只用了一千条左右的数据,方便看结果)
```




