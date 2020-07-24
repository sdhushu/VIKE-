import json
import time
import re
import threading

from selenium import webdriver
from pyquery import PyQuery as pq
from selenium.webdriver.chrome.options import Options
from PIL import Image

# 用户id
name = []
#用户默认地址
s_adress = []
#最近一次浏览时间
f_time = []
#最近浏览的商品和价格
shop = []
#购物车商品总量
cart_all = []
#购物车第一件商品
cart_first = []

result = []
sum_result = []

#获取cookie
def cookie():
    chrome_options = Options()
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--headless')
    dirver = webdriver.Chrome(options=chrome_options)
    #
    dirver.get('https://login.taobao.com/member/login.jhtml')
    dirver.find_element_by_xpath('//*[@id="login"]/div[1]/i').click()
    time.sleep(1)
    dirver.get_screenshot_as_file('login.png')
    img = Image.open('login.png')
    box = (450, 300, 750, 500)
    img = img.crop(box)
    # 保存到本地
    img.save('captcha.png')
    img.show()
    dictCookies = dirver.get_cookies()
    jsonCookies = json.dumps(dictCookies)
    with open("cookies_tao.json", "w") as fp:
        fp.write(jsonCookies)
    doc = pq(dirver.page_source)
    s_name = doc('div.s-name').text()
    print(f'用户名:{s_name}')
    sum_result.append(s_name)
    name.append(s_name)
    user_img = doc('a.s-avatar>img').attr('src')
    print(f'用户的头像地址为{user_img}')
    sum_result.append(user_img)
    dirver.close()

#收货地址
def btlogin():
    chrome_options = Options()
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--headless')
    dirver2 = webdriver.Chrome(options=chrome_options)
    dirver2.get('https://login.taobao.com/member/login.jhtml')
    dirver2.delete_all_cookies()
    with open('cookies_tao.json', 'r', encoding='utf-8') as f:
        listCookies = json.loads(f.read())
    for cookie in listCookies:
        dirver2.add_cookie({
            'domain': '.taobao.com',  # 此处xxx.com前，需要带点
            'name': cookie['name'],
            'value': cookie['value'],
            'path': '/',
            'expires': None
        })
    dirver2.get("https://www.taobao.com/markets/footmark/tbfoot")
    time.sleep(1)
    dirver2.find_element_by_xpath('//*[@id="J_SiteNavLogin"]/div[1]/div[2]/a').click()
    time.sleep(1)
    dirver2.find_element_by_link_text("我的收货地址").click()
    handle = dirver2.window_handles
    dirver2.switch_to.window(handle[-1])
    time.sleep(3)
    html = dirver2.page_source
    res = pq(html)
    # print(res)
    username = res('.next-table-cell-wrapper').text()
    username = str(username)
    result = username[27:].replace('修改|删除', '').replace('设为默认', '').split('默认地址')
    adress = []
    adress.append(result)
    print(f'收货地址数据获取成功{adress}')
    sum_result.append(adress)
    print(f'猜测您的地址为{adress[0][0]}')
    s_adress.append(adress[0][0])
    a = re.findall(r'(?<=省)(.*?)(?=市)',adress[0][0])
    print(a)
    dirver2.get('http://api.map.baidu.com/lbsapi/creatmap/')
    dirver2.find_element_by_xpath('//*[@id="searchMap"]').send_keys(a)
    dirver2.find_element_by_xpath('//*[@id="mapCenter"]/div[2]/ul/li[3]/div/span').click()
    time.sleep(1)
    dirver2.save_screenshot('adress.png')
    img = Image.open('adress.png')
    box = (300, 200, 750, 580)
    img = img.crop(box)
    # 保存到本地
    img.save('adress.png')
    dirver2.quit()

#足迹商品
def foot1():
    chrome_options = Options()
    chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
    chrome_options.add_argument('--headless')
    foot = webdriver.Chrome(options=chrome_options)
    foot.get('https://login.taobao.com/member/login.jhtml')
    foot.delete_all_cookies()
    with open('cookies_tao.json', 'r', encoding='utf-8') as f:
        listCookies = json.loads(f.read())
    for cookie in listCookies:
            foot.add_cookie({
                'domain': '.taobao.com',  # 此处xxx.com前，需要带点
                'name': cookie['name'],
                'value': cookie['value'],
                'path': '/',
                'expires': None
            })
    foot.get("https://www.taobao.com/markets/footmark/tbfoot")
    foot.execute_script("var action=document.documentElement.scrollTop=60000")
    time.sleep(2)
    foot.execute_script("var action=document.documentElement.scrollTop=60000")
    time.sleep(2)
    foot.execute_script("var action=document.documentElement.scrollTop=60000")
    time.sleep(2)
    foot.execute_script("var action=document.documentElement.scrollTop=60000")
    time.sleep(2)
    foot_html = pq(foot.page_source)
    foot_time = foot_html('.item-box.J_goods').attr('data-date')
    print(f'您最近一次逛淘宝{foot_time}')
    f_time.append(foot_time)
    foot_img = foot_html('.img-box.J_box>img').items()
    foot_box = []
    foot_price1 = []
    for x in foot_img:
        print(x.attr('src'))
    foot_title = foot_html('.title').items()
    for n in foot_title:
        foot_box.append(n.text())
    foot_price = foot_html('.price-new').items()
    for z in foot_price:
        foot_price1.append(z.text())
    print(f'足迹商品获取成功{foot_box}')
    print(f'足迹商品获取成功{foot_price1}')
    print(f'您最近浏览的商品为{foot_box[0]}')
    print(f'您最近浏览的商品价格为{foot_price1[0]}')
    sum_result.append(dict(zip(foot_box,foot_price1)))
    a = foot_box[0]
    b = foot_price1[0]
    shop.append(a)
    shop.append(b)
    foot.quit()

#购物车商品
def cart1():
    chrome_options = Options()
    chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
    chrome_options.add_argument('--headless')
    cart = webdriver.Chrome(options=chrome_options)
    cart.get('https://login.taobao.com/member/login.jhtml')
    cart.delete_all_cookies()
    with open('cookies_tao.json', 'r', encoding='utf-8') as f:
        listCookies = json.loads(f.read())
    for cookie in listCookies:
        cart.add_cookie({
                'domain': '.taobao.com',
                'name': cookie['name'],
                'value': cookie['value'],
                'path': '/',
                'expires': None
            })
    cart.get("https://cart.taobao.com/cart.htm?from=mini&ad_id=&am_id=&cm_id=&pm_id=1501036000a02c5c3739")
    cart_box = []
    cart_price1 = []
    cart_html = pq(cart.page_source)
    cart_title = cart_html('.item-basic-info>a').items()
    for i in cart_title:
        a = i.text()
        cart_box.append(a)
    cart_price = cart_html('.J_ItemSum.number').items()
    for x in cart_price:
        b = x.text()
        cart_price1.append(b)
    print('购物车数据获取成功')
    print(cart_box)
    print(cart_price1)
    sum_result.append(cart_box)
    sum_result.append(cart_price1)
    print(f'您购物车中的前1样商品为{cart_box[0]}')
    print(f'您购物车中的共有{len(cart_box)}样商品')
    c = cart_box[0]
    d = cart_price1[0]
    cart_all.append(len(cart_box))
    cart_first.append(c)
    cart_first.append(d)
    cart.quit()


#已购买的商品
def buy():
    chrome_options = Options()
    chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
    chrome_options.add_argument('--headless')
    buy = webdriver.Chrome(options=chrome_options)
    buy.get('https://login.taobao.com/member/login.jhtml')
    buy.delete_all_cookies()
    with open('cookies_tao.json', 'r', encoding='utf-8') as f:
        listCookies = json.loads(f.read())
    for cookie in listCookies:
        buy.add_cookie({
            'domain': '.taobao.com',
            'name': cookie['name'],
            'value': cookie['value'],
            'path': '/',
            'expires': None
        })
    buy.get("https://buyertrade.taobao.com/trade/itemlist/list_bought_items.htm")
    orders  =[]
    orders_html = pq(buy.page_source)
    orders_title = orders_html('span').text()
    orders.append(orders_title)
    print('订单数据获取成功')
    print(orders)
    sum_result.append(orders)
    buy.quit()



threads = []
threads.append(threading.Thread(target=btlogin))
threads.append(threading.Thread(target=foot1))
threads.append(threading.Thread(target=cart1))
threads.append(threading.Thread(target=buy))





def taobao_go():
    a = time.perf_counter()
    cookie()
    def start():
        for t in threads:
            t.start()
    start()
    b = time.perf_counter()
    print(b-a)
    time.sleep(80)
    result.append(name)
    result.append(s_adress)
    result.append(f_time)
    result.append(shop)
    result.append(cart_all)
    result.append(cart_first)
    result.append(sum_result)
    return result


# print(result)
# print('---------------------------------------')
# print(sum_result)




