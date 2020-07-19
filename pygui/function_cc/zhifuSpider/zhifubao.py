import time
from PIL import Image
from pyquery import PyQuery as pq
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
resturt=[]
class ZhiFuBao:
    def __init__(self):
        self.url = 'https://mbillexprod.alipay.com/enterprise/pcMerchYearBill19.htm#/'
        chrome_options = Options()
        chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
        chrome_options.add_argument('--headless')  # 浏览器不提供可视化页面.
        # 申明是谷歌浏览器
        global browser
        browser = webdriver.Chrome(options=chrome_options)
        browser.maximize_window()
    def go(self):
        self.login(browser)
        return resturt
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
        time.sleep(1)
        Image.open('captcha.png')
        time.sleep(15)
        self.data(browser)

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
        resturt.append(user)
        resturt.append(time)
        resturt.append(dict(zip(key, c)))
        # print(user)
        # print(time)
        # print(dict(zip(key, c)))

# if __name__ == '__main__':
#      Alipay=ZhiFuBao()
#      Alipay.go()

