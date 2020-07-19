
import time

from PIL import Image
from pyquery import PyQuery as pq
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
'''
本程序提供qq邮箱信息拉取
主入口为star_page
'''

result =[]
sum_result = []

#把程序封装成类方便调用
class QQemail:
    def __init__(self):
        self.url = 'https://mail.qq.com/'
        self.name = []
        self.qq = []
        self.group = []
        chrome_options = Options()
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--headless')
        browser = webdriver.Chrome(options=chrome_options)
        self.login(browser)

    #登录
    def login(self,browser):
        browser.get(self.url)
        browser.save_screenshot('login.png')
        img = Image.open('login.png')
        box = (450, 200, 650, 400)
        img = img.crop(box)
        # 保存到本地
        img.save('captcha.png')
        img.show()
        browser.find_element_by_xpath('//*[@id="composebtn"]').click()
        time.sleep(1)
        frame = browser.find_element_by_xpath('//*[@id="mainFrame"]')
        browser.switch_to.frame(frame)
        time.sleep(5)
        #数据清洗
        doc = pq(browser.page_source)
        title = doc('.lm_ca').items()
        # name = doc('b#useralias').text()
        group = doc('.groupclose').items()
        for x in group:
            x.attr('title')
            # print(f'分组为{x.text()}')
            self.group.append(x.text())
        print(self.group[-2:])
        result.append(self.group[-2:])

        for i in title:
            browser.find_element_by_link_text(i.attr('title')).click()
            doc1 = pq(browser.page_source)
            name = doc1('.lm_addr').items()
            for x in name:
                self.name.append(x.text())
                self.qq.append(x.attr('title'))
        print(self.name)
        sum_result.append(self.name)
        print(self.qq)
        sum_result.append(self.qq)
        print(f'您最近联系人有{self.name[:3]}')
        result.append(self.name[:3])
        print(f'他们的qq号为{self.qq[:3]}')
        result.append(self.qq[:3])
        browser.quit()

#交给gui使用
def emailgo():
    QQemail()
    #print(result)
    result.append(sum_result)
    #print(result)
    return result