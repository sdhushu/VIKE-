import time
import requests

from PIL import Image
from pyquery import PyQuery as pq
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

result=[]
sum_result = []
class Music:
    def __init__(self):
        self.url = 'https://music.163.com/'
        self.week = []
        self.num = []
        self.all_time = []
        self.all_num = []
        self.song_id = []
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
        }
        chrome_options = Options()
        chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
        chrome_options.add_argument('--headless')  # 浏览器不提供可视化页面.
        chrome_options.add_argument("--window-size=1920,1050")
        global browser
        browser = webdriver.Chrome(options=chrome_options)
        # browser.maximize_window()
        self.login(browser)
    def login(self,browser):
        browser.get(self.url)
        browser.find_element_by_link_text('登录').click()
        browser.save_screenshot('123.png')
        img = Image.open('123.png')
        box = (750, 400, 1200, 600)
        img = img.crop(box)
        img.show()
        # 保存到本地
        img.save('captcha.png')
        print('开始拉取数据')
        doc = pq(browser.page_source)
        home_url = doc('.mask').attr('href')
        self.data(browser,home_url)

    def data(self,browser,home_url):
        browser.get('https://music.163.com/'+'/user/songs/rank'+str(home_url)[10:])
        time.sleep(1)
        browser.switch_to.frame(0)
        data_html = pq(browser.page_source)
        browser.find_element_by_xpath('//*[@id="songsall"]').click()
        time.sleep(1)
        desc_html = pq(browser.page_source)
        browser.quit()
        self.data_info(data_html,desc_html)

    def data_info(self,data_html,desc_html):
        #最近一周
        week = data_html('.ttc').items()
        num  = data_html('span.times.f-ff2').items()
        song_id = data_html('span.txt>a').items()
        for x in song_id:
            self.song_id.append(x.attr('href'))
        for i in week:
            self.week.append(i.text())
        for s in num:
            self.num.append(s.text())
        #所有时间
        all_time = desc_html('.ttc').items()
        all_num = desc_html('span.times.f-ff2').items()
        all_songs = desc_html('h4').text()
        for i in all_time:
            self.week.append(i.text())
        for s in all_num:
            self.num.append(s.text())
        a = dict(zip(self.week,self.num))
        result.append(a[:3])
        sum_result.append(a)
        print(a)
        d = [k for k, v in a.items() if len(v) >= 4]
        result.append(d)
        result.append(all_songs)
        sum_result.append(all_songs)
        self.song_down()

    def song_down(self):
        c = 1
        http = requests.get('http://music.163.com/song/media/outer/url?'+self.song_id[0],headers=self.headers)
        with open(f'{c}' + '.mp3', 'wb') as f:
            f.write(http.content)

def go():
    Music()
    print(result)
    return result