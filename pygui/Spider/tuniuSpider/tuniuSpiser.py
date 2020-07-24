# -*- coding:utf-8  -*-
import time

from PIL import Image
from pyquery import PyQuery as pq
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

result = []
sum_result = []
class TuNiu:
    def __init__(self):
        self.url = 'https://i.tuniu.com/list'
        self.order_time = []
        self.order_num = []
        self.order_title = []
        self.order_people = []
        self.order_price = []
        self.order_info = []
        self.tr = []
        self.tr_info = []
        chrome_options = Options()
        chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
        chrome_options.add_argument('--headless')  # 浏览器不提供可视化页面.
        browser = webdriver.Chrome(options=chrome_options)
        self.login(browser)

    def login(self,browser):
        browser.get(self.url)
        browser.find_element_by_xpath('//*[@id="login-tab-pass"]').click()
        browser.save_screenshot('login.png')
        img = Image.open('login.png')
        box = (350, 270, 650, 500)
        img = img.crop(box)
        img.save('captcha.png')
        img.show()
        print('请扫码  15秒')
        cookies = browser.get_cookies()
        print(cookies)
        html = pq(browser.page_source)
        order_num = html('.order-id').items()
        for a in order_num:
            self.order_num.append(a.text())
        id = []
        for i in self.order_num:
            id.append(i[4:])
        for i in id:
            browser.get('http://www.tuniu.com/tn?r=user/user/neworderdetail&id='+i)
            doc = pq(browser.page_source)
            user_adress = doc('.panel-left').text()
            come_home = doc('.panel-middle').text()
            user = doc('.time').text()
            traveling = doc('.name').items()
            traveling_info = doc('.flight-journey>ul').items()
            for i in traveling:
                self.tr.append(i.text())
            for s in traveling_info:
                self.tr_info.append(s.text())
            print(f'机场出发地{user_adress}')
            print(f'归来时间{come_home}')
            print(f'联系人{user}')
            print(f'出游人姓名{self.tr}')
            print(f'出游人信息{self.tr_info}')
            sum_result.append([user_adress,come_home,user,self.tr,self.tr_info])
            time.sleep(1)
        browser.quit()
        self.data(html)

    def data(self,html):
        order_time = html('.item-time').items()
        order_num = html('.order-id').items()
        order_title = html('.item-desc>p').items()
        order_people = html('.item-mount').items()
        order_price = html('.item-price').items()
        order_info = html('.item-statue').items()
        for a in order_time:
            self.order_time.append(a.text())
        for a in order_num:
            self.order_num.append(a.text())
        for a in order_title:
            self.order_title.append(a.attr('title'))
        for a in order_people:
            self.order_people.append(a.text())
        for a in order_price:
            self.order_price.append(a.text())
        for a in order_info:
            self.order_info.append(a.text())

        print(self.order_time)
        sum_result.append(self.order_time)
        print(self.order_num)
        sum_result.append(self.order_num)
        print(self.order_title)
        sum_result.append(self.order_title)
        print(self.order_people)
        sum_result.append(order_people)
        print(self.order_price)
        sum_result.append(order_price)
        print(self.order_info)
        sum_result.append(order_info)
        print(f'您最近一次下单时间{self.order_time[0]}')
        print(f'您最近一次出游时间{self.order_time[1]}')
        print(f'您最近一次订单编号{self.order_num[0]}')
        print(f'您最近一次出游的地点{self.order_title[0][1:12]}')
        print(f'您最近一次出游的人数{self.order_people[0]}')
        print(f'您最近一次出游的加个{self.order_price[0]}')
        print(f'您最近一次订单的状态{self.order_info[0][:4]}')
        result.append(self.order_time[0][5:])
        result.append(self.order_time[1])
        result.append(self.order_num[0][4:])
        result.append(self.order_title[0][1:12])
        result.append(self.order_people[0])
        result.append(self.order_price[0])
        result.append(self.order_info[0][:4])

def tuniugo():
    TuNiu()
    #print(result)
    result.append(sum_result)
    #print(result)
    return result