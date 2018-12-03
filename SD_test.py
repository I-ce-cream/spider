import requests
import time
from bs4 import BeautifulSoup

def get_html(url):
    try:
        r = requests.get(url,timeout=10)
        #设置编码
        #r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return "ERROR"

def get_content(url):
    comments = []
    html = get_html(url)
    soup = BeautifulSoup(html,'lxml')
    
    list_tags = soup.find_all('li',class_ = ' j_thread_list clearfix')
    
    for tag in list_tags:
        comment = {}
        try:
            comment['title'] =tag.find('a',class_ = 'j_th_tit').text.strip()
            comment['link'] ='http://tieba.baidu.com/'+ tag.find()
            comment['name'] =
            comment['time'] =
            comment['replyNum'] =
            comments.append(comment)
        except:
            print('出了点小问题')
    return comments

def saveFile(dict):
    #with open ... as  读写文档
    with open('SD.txt','a+') as f:
        for comment in dict:
            f.write('标题：{} \t 链接：{} \t 发帖人：{} \t 发帖时间：{} \t 回复数量：{} \n '.format(
                comment['title'], comment['link'], comment['name'], comment['time'], comment['replyNum']))
    print('当前页面保存完毕')



def main(base_url,page):
    list_url = []
    for i in range(0,page):
        list_url.append(base_url + '&pn=' + str(50 * i))
    print('网页列表保存完毕，开始筛选信息')

    for url in list_url:
        content = get_content(url)
        saveFile(content)
    print('信息保存完毕')



base_url = 'https://tieba.baidu.com/f?kw=sd%E6%95%A2%E8%BE%BE&ie=utf-8'
page = 3

if __name__ == '__main__':
    main(base_url,page)