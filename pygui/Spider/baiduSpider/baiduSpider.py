# coding=utf-8
import time
import re
import requests

from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

'''
本页面提供百度个人数据抓取
主入口为star_page.py
'''

result = []
sum_result = []
#把抓取程序封装成类 方便调用
class BaiDu:
    #初始化属性
    def __init__(self):
        self.url = 'https://www.baidu.com/'
        chrome_options = Options()
        chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
        chrome_options.add_argument('--headless')  # 浏览器不提供可视化页面.
        chrome_options.add_argument("--window-size=1920,1050")
        browser = webdriver.Chrome(options=chrome_options)
        self.login(browser)

    #用selenium进行登录界面操作
    def login(self,browser):
        browser.get(self.url)
        browser.find_element_by_link_text('登录').click()
        time.sleep(3)
        browser.save_screenshot('login.png')
        img = Image.open('login.png')
        box = (750, 400, 1100, 600)
        img = img.crop(box)
        # 保存到本地
        img.save('captcha.png')
        img.show()
        print('请扫码-----------')
        cookies = browser.get_cookies()
        browser.quit()
        #将cookie保存到本地 传递给下一个函数使用
        cookie = [item["name"] + "=" + item["value"] for item in cookies]
        cookiestr = ';'.join(item for item in cookie)
        self.data(cookiestr)

    #获取个人数据
    def data(self,cookiestr):
        headers = {
            "Cookie": cookiestr,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
        }
        for i in range(1,6):
            url = f'https://www.baidu.com/recsys/hisproxy/data/usrhistory?page={i}'
            http = requests.get(url,headers=headers)
            a = http.text.encode('utf-8').decode('unicode_escape')
            # print(f'时间:{a[68:80]}')
            # print(a[80:])
            c = re.findall(r'"query":"(.*?)"',a,re.S)
            d = re.findall(r'"time":"(.*?)"',a,re.S)
            # print(f'您最近一次的查询时间是{d[0]}')
            result.append(d[0])
            # print(f'您这天查询的前三条关键字为{c[:3]}')
            result.append(c[:3])
            # print(f'查询时间为{a[68:80]}{d[:3]}')
            result.append([a[68:80],d[:3]])
            # print(f'您这天的查询次数为{len(c)}')
            result.append(len(c))
            sum_result.append(a[68:])
            sum_result.append(c)
            sum_result.append(d)




#交给gui界面使用
def baidu_go():
    a = time.perf_counter()
    BaiDu()
    b = time.perf_counter()
    result.append(sum_result)
    print(result)
    return result