import requests

from pyquery import PyQuery as pq
from aip import AipOcr
from PIL import ImageFilter
from PIL import Image
resturt=[]
class Login(object):
    def __init__(self,name,password):
        self.headers = {
            'Referer':'https://account.chsi.com.cn/passport/login?service=https%3A%2F%2Fmy.chsi.com.cn%2Farchive%2Fj_spring_cas_security_check',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
            'Host':'account.chsi.com.cn'
        }
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
        }
        self.prarms = {
            'trnd': 1593923253028,
        }
        self.APP_ID = '21139008'
        self.API_KEY = '9S5htfoQdGKfn2wI21R1G5jn'
        self.SECRET_KEY = 'pbGVKG13CDrp4WLhwmOHV6XIv2D3XyYh'
        self.login_url = 'https://account.chsi.com.cn/passport/login'
        self.i = []
        # self.post_url = 'https://account.chsi.com.cn/passport/login?service=https%3A%2F%2Fmy.chsi.com.cn%2Farchive%2Fj_spring_cas_security_check'
        self.logined_url = 'https://my.chsi.com.cn/archive/gdjy/xj/show.action'
        self.username = name
        self.password = password
        self.session = requests.session()

    def xx(self):
        self.token()
        return resturt
    def token(self):
        response = self.session.get(self.login_url,headers=self.headers)
        response.encoding = 'utf-8'
        all = []
        html = pq(response.text)
        a = html('input').items()
        for i in a:
            all.append(i.attr('value'))
        lt = all[3]
        execution = all[4]
        print(response.status_code)
        self.login(lt,execution)

    def login(self,lt,execution):
        post_data ={
            'username':self.username,
            'password':self.password,
            'lt':lt,
            'execution':execution,
            '_eventId': 'submit',
            'submit': '登  录'
        }
        try:
            response = self.session.post(self.login_url,data=post_data,headers=self.headers)
            response.encoding = 'utf-8'
            # cookie = self.session.cookies.get_dict()
            self.info()
        except Exception:
            print('请输入正确用户名密码!')

    def info(self):
        response = self.session.get('https://my.chsi.com.cn/archive/gdjy/xj/show.action',params=self.prarms,headers=self.header)
        response.encoding = 'utf-8'
        doc = pq(response.text)
        self.data(doc)

    #数据拉取
    def data(self,doc):
        data_img = doc('.xjxx-img').attr('src')
        user_img = doc('.pic>img').attr('src')
        user_img = 'https://my.chsi.com.cn/' + user_img
        print(data_img,user_img)
        self.save_img(data_img,user_img)

    #图片存储
    def save_img(self,data_img,user_img):
        data = self.session.get(data_img,headers=self.header)
        with open('data_info'+'.jpg', 'wb') as f:
            f.write(data.content)

        user = self.session.get(user_img, headers=self.header)
        with open('user_info'+'.jpg', 'wb') as f:
            f.write(user.content)
        self.get_file_content()

    #图片识别
    def get_file_content(self):
        with open('data_info.jpg', 'rb') as fp:
            a = fp.read()
        client = AipOcr(self.APP_ID, self.API_KEY, self.SECRET_KEY)
        message = client.basicAccurate(a)  # 返回识别结果
        res = message['words_result']
        for s in range(18):
            self.i.append(res[s]['words'])
            resturt.append(res[s]['words'])
        #print(self.i)
        #self.img_text()


    #图片处理
    def img_text(self):
        square = Image.open("user_info.jpg")
        square1 = square.filter(ImageFilter.CONTOUR)
        square1.save("user_info.jpg")

#
# if __name__ == '__main__':
#    Login()
#    print(resturt)
