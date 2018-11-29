from bs4 import BeautifulSoup
import test1
import requests

txt = test1.getHtmlText('http://www.baidu.com')

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
</html>
"""

soup = BeautifulSoup(html,'html.parser')

#print(soup.prettify())
a = soup.prettify()

#找到文档的title
b = soup.title
# <title>The Dormouse's story</title>

#title的name值
c = soup.title.name
# u'title'

#title中的字符串String
d = soup.title.string
# u'The Dormouse's story'

#title的父亲节点的name属性
e = soup.title.parent.name
# u'head'

#文档的第一个找到的段落
f = soup.p
# <p class="title"><b>The Dormouse's story</b></p>

#找到的p的class属性值
g = soup.p['class']
# u'title'

#找到a标签
h = soup.a
# http://example.com/elsie" id="link1">Elsie

#找到所有的a标签
i = soup.find_all('a')
# [http://example.com/elsie" id="link1">Elsie,
#  http://example.com/lacie" id="link2">Lacie,
#  http://example.com/tillie" id="link3">Tillie]

#找到id值等于3的a标签
j = soup.find(id="link3")
# http://example.com/tillie" id="link3">Tillie
print(j)

#我们可以通过get_text 方法 快速得到源文件中的所有text内容。
#print(soup.get_text())

#href 连接  获取所有<a>标签
#for link in soup.find_all('a'):
#    print(link.get('href'))

#get_text() 获得源文件中所有text内容