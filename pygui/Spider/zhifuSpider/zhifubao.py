import time

from PIL import Image

from pyquery import PyQuery as pq
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class ZhiFuBao:
    def __init__(self):
        self.url = 'https://mbillexprod.alipay.com/enterprise/pcMerchYearBill19.htm#/'
        self.url2 = 'https://mbillexprod.alipay.com/enterprise/pcYearBill.htm'
        self.y1  =[]
        self.y2 = []
        chrome_options = Options()
        chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
        chrome_options.add_argument('--headless')  # 浏览器不提供可视化页面.
        browser = webdriver.Chrome()
        self.login(browser)

    def login(self,browser):
        browser.get(self.url)
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="J-loginMethod-tabs"]/li[1]').click()
        browser.get_screenshot_as_file('zhifu.png')
        img = Image.open('zhifu.png')
        box = (350, 200, 650, 400)
        img = img.crop(box)
        img.show()
        # 保存到本地
        img.save('captcha.png')
        print('二维码已保存到本地 请在20秒内扫码')
        input('输入二维码后请回车-----------------')
        self.data(browser)
        self.data_2(browser)
        self.predict()

    #2019年账单
    def data(self,browser):
        data_html = pq(browser.page_source)
        username = data_html('.userName___2wHhz').text()
        data_time = data_html('.utilDate___3iD69').text()
        all_year = data_html('.amountGroup___Im4Rh>span').text()
        browser.execute_script("var action=document.documentElement.scrollTop=1500")
        browser.save_screenshot('data.png')
        user = {'用户名':username}
        time = {'账单时间':data_time}
        key = '全年交易额 全年顾客 全年收入 全年收入总金额 全年支出总金额 全年日均余额 月均账户收入 月均账户支出(元) ' \
              '全年总成交金额(元) 总成交笔数(笔) 全年总退款金额(元) 总退款笔数(笔) 总实收金额(元) 平均笔单价(元) 日均成交金额(元) ' \
              '日均成交笔数 全年总顾客数(人) 老顾客总数(人) 新顾客总数(人) 人均消费金额(元) 人均消费笔数(笔) 累计最高消费金额(元) 累计最高消费笔数(笔)'
        all_year = all_year.split(' ')
        key = key.split(' ')
        c = []
        for i in all_year:
            if i == '':
                pass
            else:
                c.append(i)
        print(user)
        print(time)
        print(dict(zip(key, c)))
        self.y1.append(c[2])



    #2017年账单
    def data_2(self,browser):
        browser.get(self.url2)
        data_2_html = pq(browser.page_source)
        username = data_2_html('div.userName___W_wA8>span').text()
        data_time = data_2_html('.utilDate___3MbMV').text()
        all_year = data_2_html('span.yearRecordItemAmount___12Hxy').text()
        browser.execute_script("var action=document.documentElement.scrollTop=1500")
        browser.save_screenshot('data.png')
        user = {'用户名': username}
        time = {'账单时间': data_time}
        key = '全年交易额 全年顾客 全年收入 全年收入总金额 全年支出总金额 全年日均余额 月均账户收入 月均账户支出(元) ' \
              '全年总成交金额(元) 总成交笔数(笔) 全年总退款金额(元) 总退款笔数(笔) 总实收金额(元) 平均笔单价(元) 日均成交金额(元) ' \
              '日均成交笔数 全年总顾客数(人) 老顾客总数(人) 新顾客总数(人) 人均消费金额(元) 人均消费笔数(笔) 累计最高消费金额(元) 累计最高消费笔数(笔)'
        all_year = all_year.split(' ')
        key = key.split(' ')
        c = []
        for i in all_year:
            if i == '':
                pass
            else:
                c.append(i)
        print(user)
        print(time)
        print(dict(zip(key, c)))
        self.y2.append(c[2])

    #线性回归预测
    def predict(self):
        print(self.y1,self.y2)
        x1 = 2017
        x2 = 2019
        x = 2018
        y1 =float(self.y1[0].replace(',',''))
        y2 = float(self.y2[0].replace(',',''))
        y = (y1+y2)/2
        c= (x1-x)*(y1-y)+(x2-x)*(y2-y)
        s = (x1-x)*(x1-x)+(x2-x)*(x2-x)
        b = s/c
        a = y-b*2018
        y3 = b*2020+a
        print(f'预测2020年您的收入是{y3}')


if __name__ == '__main__':
    a = time.perf_counter()
    ZhiFuBao()
    b = time.perf_counter()
    print(b-a)



