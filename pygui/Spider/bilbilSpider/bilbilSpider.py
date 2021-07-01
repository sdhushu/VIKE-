import time

from PIL import Image
from pyquery import PyQuery as pq
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

print('欢迎使用艾伦爬虫程序')
result = []
sum_result = []
class BilBil:
    def __init__(self):
        self.url = 'https://passport.bilibili.com/login'
        self.title = []
        self.watch_time = []
        self.type = []
        self.username = []
        chrome_options = Options()
        chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
        chrome_options.add_argument('--headless')  # 浏览器不提供可视化页面.
        browser = webdriver.Chrome(options=chrome_options)
        # browser.maximize_window()
        self.login(browser)

    def login(self,browser):
        browser.get(self.url)
        time.sleep(2)
        browser.save_screenshot('login.png')
        img = Image.open('login.png')
        box = (150, 260, 350, 460)
        img = img.crop(box)
        img.save('captcha.png')
        img.show()
        self.data(browser)
        self.user_info(browser)

    def data(self,browser):
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="internationalHeader"]/div[1]/div/div[3]/div[2]/div[6]/span/div[2]/span/span').click()
        handle = browser.window_handles
        browser.switch_to.window(handle[-1])
        time.sleep(1)
        for i in range(4):
            browser.execute_script("var action=document.documentElement.scrollTop=60000")
            time.sleep(2)
        doc =pq(browser.page_source)
        title = doc('.title').items()
        watch_time = doc('.lastplay-t').items()
        video_type = doc('.name').items()
        username = doc('span.username').items()
        for i in title:
            self.title.append(i.text())
        for x in watch_time:
            self.watch_time.append(x.text())
        for s in video_type:
            self.type.append(s.text())
        for z in username:
            self.username.append(z.text())
        print(self.username)
        print('------------')
        print(self.type[122:])
        print(type(self.type[122:]))
        dict1 = {}
        for i in self.type[122:]:
            if i not in dict1.keys():
                dict1[i] = self.type[122:].count(i)
        name =max(dict1,key=dict1.get)

        dict2  ={}
        for x in self.username:
            if x not in dict2.keys():
                dict2[x] = self.username.count(x)
            user1 = max(dict2, key=dict2.get)
        print(f'视频名{self.title}')
        print(f'观看时间{self.watch_time}')
        print(f'视频类型{self.type[122:]}')
        print(f'您最后一次登录时间为{self.watch_time[0]}')
        print(f'您最喜欢观看的视频系列为: {name}')
        print(f'您最喜欢的博主为: {user1}')
        sum_result.append(self.watch_time)
        sum_result.append(self.title)
        sum_result.append(self.type[122:])
        result.append(self.watch_time[0])
        result.append(name)
        result.append(user1)



    def user_info(self,browser):
        browser.get('https://space.bilibili.com/')
        time.sleep(1)
        handle = browser.window_handles
        browser.switch_to.window(handle[-1])
        browser.save_screenshot('user.png')
        doc = pq(browser.page_source)
        username = doc('#h-name').text()
        word = doc('.h-sign').attr('title')
        print(f'用户名为:{username}')
        sum_result.append(username)
        result.append(username)
        sum_result.append(word)
        print(f'个性签名为:{word}')
        result.append(word)
        browser.quit()







def bilibili_go():
    BilBil()
    result.append(sum_result)
    return result
