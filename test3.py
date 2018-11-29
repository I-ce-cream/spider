import bs4

soup = bs4.BeautifulSoup(open('alice.html'),'lxml')

#print(soup.prettify())

#设置编码类型
#soup = BeautifulSoup(markup,from_encoding="编码方式")

#head_tag = soup.body
#print(head_tag.contents)
#for child in head_tag.children:
#    print(child)
'''
head_tag = soup.head
for child in head_tag.descendants:
    print(child)
'''
#对象的种类：
#bs4 库将复杂的html文档转化为一个复杂的树形结构，每个节点都是Python对象 ，所有对象可以分为以下四个类型：Tag , NavigableString , BeautifulSoup , Comment
#我们来逐一解释：

#Tag： 和html中的Tag基本没有区别，可以简单上手使用
#NavigableString： 被包裹在tag内的字符串
#BeautifulSoup： 表示一个文档的全部内容，大部分的时候可以吧他看做一个tag对象，支持遍历文档树和搜索文档树方法。
#Comment：这是一个特殊的NavigableSting对象，在出现在html文档中时，会以特殊的格式输出，比如注释类型。

#获取所有的标签 find_all()

#tag的.contents属性可以将tag的子节点以列表的方式输出

#另外通过tag的 .children生成器，可以对tag的子节点进行循环

#tag的.descendants用来遍历子孙节点
#for child in head_tag.descendants:
#    print(child)

#如果该tag只有一个子节点（NavigableString类型）：直接使用tag.string就能找到。
#如果tag有很多个子、孙节点，并且每个节点里都string：
#找出tag下子 孙 节点所有文本内容
for string in soup.strings:
    print(repr(string))