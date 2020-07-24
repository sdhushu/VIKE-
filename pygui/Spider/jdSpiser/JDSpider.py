# coding:utf-8
import time

from PIL import Image
from pyquery import PyQuery as pq
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

result = []
sum_result = []
class JD:
    def __init__(self):
        self.order_title = []
        self.order_time = []
        self.order_price = []
        self.adress_label = []
        self.adress_info = []
        self.cart_title = []
        self.cart_price = []
        self.url = 'https://order.jd.com/center/list.action'
        chrome_options = Options()
        chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
        chrome_options.add_argument('--headless')  # 浏览器不提供可视化页面.
        chrome_options.add_argument("--window-size=1920,1050")
        browser = webdriver.Chrome(options=chrome_options)

        self.order(browser)

    def order(self,browser):
        browser.get(self.url)
        browser.save_screenshot('JD.png')
        img = Image.open('JD.png')
        # box = (950, 300, 1300, 700)
        box = (1050, 200, 1500, 600)
        img = img.crop(box)
        # 保存到本地
        img.save('jdlogin.png')
        img.show()
        self.order_data(browser)

#订单页数据拉取
    def order_data(self,browser):
        order_html = pq(browser.page_source)
        order_title = order_html('.a-link').items()
        order_time = order_html('.dealtime').items()
        order_price = order_html('.amount>span').items()
        for i in order_title:
            self.order_title.append(i.text())
        for x in order_time:
            self.order_time.append(x.text())
        for s in order_price:
            self.order_price.append(s.text())
        self.adress(browser)

#地址页数据拉取
    def adress(self,browser):
        try:
            browser.find_element_by_xpath('//*[@id="_MYJD_add"]/a').click()
            time.sleep(1)
        except Exception:
            print('二维码失效 请重新打开本程序')
            browser.close()
        time.sleep(3)
        adress_html = pq(browser.page_source)
        adress_info = adress_html('.fl').items()
        for x in adress_info:
            self.adress_info.append(x.text())
        self.cart(browser)

#购物车数据拉取
    def cart(self,browser):
        try:
            browser.find_element_by_xpath('//*[@id="settleup-2014"]/div[1]').click()
        except Exception:
            print('访问过于频繁 请稍后再试')
            browser.close()
        handle = browser.window_handles
        browser.switch_to.window(handle[-1])
        time.sleep(1)
        cart_html = pq(browser.page_source)
        cart_title = cart_html('.p-name').items()
        cart_price = cart_html('.cell.p-sum>strong').items()
        for i in cart_title:
           self.cart_title.append(i.text())
        for x in cart_price:
            self.cart_price.append(x.text())
        self.data_clear(browser)

#数据清洗
    def data_clear(self,browser):
        num = len(self.cart_price)
        self.adress_info = self.adress_info[13:]
        for i in self.adress_info:
            if i == ' ':
                pass
            else:
                self.adress_label.append(i)
        print(f'您的所有地址为{self.adress_label}')
        sum_result.append(self.adress_label)
        result.append(self.adress_label[1:4])
        print(f'您最近的下单时间为{self.order_time[0]},购买了{self.order_title[0]}')
        sum_result.append(self.order_time)
        sum_result.append(self.order_title)
        result.append(self.order_time[0])
        result.append(self.order_title[0][:10]+'...')
        print(f'近期购买商品为{self.order_title}')
        result.append(self.order_title[0])
        b = []
        for i in self.order_price[::2]:
            a = float(i.replace('¥', ''))
            b.append(a)
        print(f'近期购买商品价格总和为{sum(b)}元')
        sum_result.append(sum(b))
        result.append(sum(b))
        cart_all = dict(zip(self.cart_title[:num],self.cart_price))
        print(f'购物车数据{cart_all}')
        sum_result.append(cart_all)
        print(cart_all)
        result.append(list(cart_all.keys())[0])
        result.append(list(cart_all.values())[0])

        # print(type(cart_all))
        # result.append(cart_all[0])
        # print(self.cart_title)
        # print(self.cart_price)
        browser.quit()

def jdgo():
    JD()
    # print(result)
    result.append(sum_result)
    # print(result)
    return result
