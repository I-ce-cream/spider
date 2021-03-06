import requests

'''
r = requests.get("http://www.baidu.com")

#HTTP请求的返回状态，比如，200表示成功，404表示失败
print (r.status_code)
#HTTP请求中的headers
print (r.headers)
#从header中猜测的响应的内容编码方式 
print (r.encoding)
#从内容中分析的编码方式（慢）
print (r.apparent_encoding)
#响应内容的二进制形式
print (r.content)
'''

#requests 抓取网页通用框架
def getHtmlText(url):
    try:
        r = requests.get(url,timeout=30)
        # 如果状态码不是200 则应发HTTOError异常
        r.raise_for_status()
        # 设置正确的编码方式
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "Something Wrong"


#print(getHtmlText('http://www.baidu.com'))

#requests.request() 构造一个请求，支撑以下各方法的基础方法
#requests.get()     获取HTML网页的主要方法，对应于HTTP的GET
#requests.head()    获取HTML网页头信息的方法，对应于HTTP的HEAD
#requests.post()    向HTML网页提交POST请求的方法
#requests.put()     向HTML网页提交PUT请求的方法
#requests.patch()   向HTML网页提交局部修改请求
#requests.delete()  向HTML网页提交删除请求

#requests.get
#get(url, params=None, **kwargs)
'''
kwargs: 控制访问的参数，均为可选项

params : 字典或字节序列，作为参数增加到url中

data : 字典、字节序列或文件对象，作为Request的内容 json : JSON格式的数据，作为Request的内容

headers : 字典，HTTP定制头

cookies : 字典或CookieJar，Request中的cookie

auth : 元组，支持HTTP认证功能

files : 字典类型，传输文件

timeout : 设定超时时间，秒为单位

proxies : 字典类型，设定访问代理服务器，可以增加登录认证

allow_redirects : True/False，默认为True，重定向开关

stream : True/False，默认为True，获取内容立即下载开关

verify : True/False，默认为True，认证SSL证书开关

cert : 本地SSL证书路径

url: 拟更新页面的url链接

data: 字典、字节序列或文件，Request的内容

json: JSON格式的数据，Request的内容
'''
