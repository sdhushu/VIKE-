from tkinter import Tk
import time
import tkinter as tk
# from docx import Document
from Allen.guii.function_cc.zhifuSpider.zhifubao import ZhiFuBao
from Allen.guii.Spider.taobaoSpider.taobao2 import taobao_go
from Allen.guii.Spider.bilbilSpider.bilbilSpider import BilBil
from Allen.guii.Spider.meituanSpider.meituanSpider import MeiTuan
from Allen.guii.Spider.musicSpider.musicSpider import go
from Allen.guii.function_cc.studySpider.studySpider import Login
from Allen.guii.Spider.qqemailSpider.qq_emailSpiser import QQemail
from Allen.guii.Spider.baiduSpider.baiduSpider import BaiDu
from tkinter.messagebox import *
import tkinter.messagebox
import threading
import webbrowser
from PIL import Image,ImageTk
from playsound import playsound
root=Tk()
root.geometry('1000x650')
root.resizable(0,0)
root.title('alun')
root.resizable(width=True, height=True)
frame_class=[]
def frame_group():
    specification=[(1000,90),(180,530),(820,530),(1000,30)]#容器规格，(标题栏，工具栏，首页,底部状态)
    specification_place=[(-2,0),(0,90),(180,90),(0,620)]
    # color=['#0000FF','#0000CD','#191970' ,'#00008B','#000080','#4169E1','#6495ED','#B0C4DE','#778899','#708090','#1E90FF','red']
    for i in specification:
        width=i[0]
        height=i[1]
        frame=tk.Frame(root, width=width, height=height,)
        frame_class.append(frame)
    for i1,i2 in zip(frame_class,specification_place):
        i1.place(x=i2[0],y=i2[1])
frame_group()
#底部状态栏
bar_title=tk.Label(frame_class[3],text='版本号1.1.0',width=14, height=1)
bar_title.place(x=0,y=0)
bar_title=tk.Label(frame_class[3],text='进度:',width=4, height=1)
bar_title.place(x=653,y=0)
bar_canvas = tk.Canvas(frame_class[3], width=240, height=20, bg="#F5F5F5", borderwidth=0)
bar_canvas.place(x=700,y=0)

#状态栏函数
def change_schedule(now_schedule, all_schedule):
    bar_canvas.coords(fill_rec, (5, 5, 6 + (now_schedule / all_schedule) * 240, 25))
    root.update()
    mini.set(str(round(now_schedule / all_schedule * 100, 2)) + '%')
    if round(now_schedule / all_schedule * 100, 2) == 100.00:
        mini.set("完成")
# 进度条以及完成程度
mini = tk.StringVar()
user_date= tk.StringVar()
out_rec = bar_canvas.create_rectangle(5, 5, 240, 25, outline="blue", width=1)
fill_rec = bar_canvas.create_rectangle(5, 5, 5, 25, outline="", width=0, fill="blue")
tk.Label(frame_class[3], textvariable=mini).place(x=950,y=0)
tk.Label(frame_class[3], textvariable=user_date).place(x=350,y=0)
#11个容器
color=['#0000FF','#0000CD','#191970' ,'#00008B','#000080','#4169E1','#6495ED','#B0C4DE','#778899','#708090','#1E90FF','red']
second_level_class=[]
f_home=frame_class[2]#首页
for i in range(14):
    f=tk.Frame(f_home,width=820,height=560)
    f.place(x=0,y=0)
    second_level_class.append(f)

#子页面控制
def IO(io):
    change_schedule(0, 100)
    for i in second_level_class:
        i.place_forget()
    io.place(x=0,y=0)
    print(i)
#top
f_top=frame_class[0]#标题栏
topimg=tk.PhotoImage(file='img/topimg.png')
l_topimg=tk.Label(f_top,image=topimg).place(x=5,y=0)

#tool
f_tool=frame_class[1]
toolimg=tk.PhotoImage(file='img/tool.png')
l_toolimg=tk.Label(f_tool,image=toolimg).place(x=0,y=0)
#工具栏控件
f_tool=frame_class[1]
icon_class=[]
button_class =[]
def set_toolicon():
    icon_path = ['img/icon10.png', 'img/icon9.png', 'img/icon8.png', 'img/icon7.png', 'img/icon6.png', 'img/icon5.png',
                 'img/icon4.png', 'img/icon3.png', 'img/icon2.png', 'img/icon1.png','img/icon0.png','img/icon00.png']#素材地址
    for i in icon_path:
        icon = tk.PhotoImage(file=i)
        icon_class.append(icon)
    button0=tk.Button(f_tool,image =icon_class[0],command=lambda :IO(second_level_class[0])).place(x=5,y=5)
    button1 =tk.Button(f_tool, image=icon_class[1], command=lambda: IO(second_level_class[1])).place(x=5, y=47)
    button2 = tk.Button(f_tool, image=icon_class[2], command=lambda: IO(second_level_class[2])).place(x=5, y=89)
    button3 = tk.Button(f_tool, image=icon_class[3], command=lambda: IO(second_level_class[3])).place(x=5, y=131)
    button4 = tk.Button(f_tool, image=icon_class[4], command=lambda: IO(second_level_class[4])).place(x=5, y=173)
    button5 = tk.Button(f_tool, image=icon_class[5], command=lambda: IO(second_level_class[5])).place(x=5, y=215)
    button6 = tk.Button(f_tool, image=icon_class[6], command=lambda: IO(second_level_class[6])).place(x=5, y=257)
    button7 = tk.Button(f_tool, image=icon_class[7], command=lambda: IO(second_level_class[7])).place(x=5, y=299)
    button8 = tk.Button(f_tool, image=icon_class[8], command=lambda: IO(second_level_class[8])).place(x=5, y=341)
    button9 = tk.Button(f_tool, image=icon_class[9], command=lambda: IO(second_level_class[9])).place(x=5, y=383)
    button10 = tk.Button(f_tool, image=icon_class[10], command=lambda: IO(second_level_class[10])).place(x=5, y=425)
    button11 = tk.Button(f_tool, image=icon_class[11], command=lambda: IO(second_level_class[11])).place(x=5, y=476)
set_toolicon()
#写文件
def savepage(page, tite):
    file = Document()
    file.add_heading(str(tite), level=2)
    paragraph = file.add_paragraph(str(page))
    paragraph.add_run('来源').bold = True
    file.save(str(tite) + 'testDoc.docx')
    print('成功')
#11个页面背景图片设置
#['Alipay', 'taobao', 'bilibili', 'baidu', 'tuniu', 'boos', 'netease cloud', 'Meituan', 'xuexingnet', 'jingdong', 'about us']
img_class=[]
def set_secandpage_img():
    page_secand_img = ['img/01.png', 'img/02.png', 'img/03.png', 'img/04.png', 'img/05.png', 'img/06.png', 'img/07.png',
                       'img/08.png', 'img/09.png', 'img/10.png']
    for i in page_secand_img:
        img = tk.PhotoImage(file=i)
        img_class.append(img)
    for i ,page in zip(img_class,second_level_class):
        img_sit = tk.Label(page, image=i,compound = tk.CENTER,borderwidth=0).place(x=0, y=0)
set_secandpage_img()

#小套路
def time2():
    time.sleep(15)
    for i in range(10,83):
        time.sleep(0.1)
        change_schedule(i, 100)
# 详细数据
def opendatas(path):
    webbrowser.open(path)

def date():
    dates=['正在部署爬虫','正在拉起登陆窗口','正在处理登陆信息','爬虫准备中','正在爬虫','正在获取数据标签','正在获取数据']
    for i in dates:
        time.sleep(2)
        user_date.set(i)
        time.sleep(3)
#支付宝：
f_alipay=second_level_class[0]

re_value=[]

def Alipay():

    def str_Alippay():
        new_Alipay = ZhiFuBao()
        resturd = new_Alipay.go()
        user_data_values = (list(resturd[0].values()))
        print(user_data_values)
        time_data_values = (list(resturd[1].values()))
        print(time_data_values)
        goods_data_values = (list(resturd[2].values()))
        re_value = goods_data_values
        # print(len(goods_data_values),len(re_value))
        # print(re_value)
        var1.set('用户名:' + str(user_data_values[0]))
        var2.set('账单时间:' + str(time_data_values[0]))
        time.sleep(2)
        for i in range(83, 100):
            time.sleep(0.3)
            change_schedule(i, 100)
        e = 0
        for x in sit_x:
            for y in sit_y:
                laber = tk.Label(f_alipay, justify='left', wraplength=780, text=re_value[e], font=('Arial', 25),
                                 bg='#FFFFFF', fg='#000000').place(x=x, y=y+20)
                e = e + 1



    mm = askokcancel('提示', '操作之前，请打开您的支付宝扫一扫功能，准备识别二维码')
    if mm == True:
        print('开始啦')
        for i in range(10):
            change_schedule(i, 100)
        new_Alipay = threading.Thread(target=str_Alippay)  # target是要执行的函数名（不是函数），args是函数对应的参数，以元组的形式存在
        t1 = threading.Thread(target=date)
        t2 = threading.Thread(target=time2)
        new_Alipay.start()
        t1.start()
        t2.start()
        resturd = new_Alipay
    else:
        print('tuichul')
        pass

var1=tk.StringVar()
var2=tk.StringVar()
var3=tk.StringVar()
var1.set('用户名:'+'____')
var2.set('账单时间:'+'-----')
e_values=['**,**,**','**,**,**','**,**,**','**,**,**','**,**,**','**,**,**','**,**,**','**,**,**','**,**,**','**,**,**','**,**,**','**,**,**','**,**,**','**,**,**','**,**,**','**,**,**',]
re_keys=['全年交易额:','全年顾客:','全年收入:','全年收入总金额:','全年支出总金额:','全年日均余额:','月均账户收入:','月均账户支出(元):','全年总成交金额(元):','总成交笔数(笔):','全年总退款金额(元):','总退款笔数(笔):','总实收金额(元):','平均笔单价(元):','日均成交金额(元):','日均成交笔数:','全年总顾客数(人):','老顾客总数(人):','新顾客总数(人):','人均消费金额(元):','人均消费笔数(笔):','累计最高消费金额(元):','累计最高消费笔数(笔):',]
var1.set('用户名:'+'____')
var2.set('账单时间:'+'-----')
sit_x=[40,240,440,640]
sit_y=[250,310,370,430,]
a = 0
for x in sit_x:
    for y in sit_y:
        laber = tk.Label(f_alipay, justify='left', wraplength=780, text=re_keys[a], font=('Arial', 11),
                     bg='#FFFFFF', fg='#000000').place(x=x, y=y)
        a=a+1
alipay_user=tk.Label(f_alipay,textvariable=var1,font=('Arial', 25),bg='#FFFFFF',fg='#000000').place(x=40,y=150)
alipay_billtime=tk.Label(f_alipay,textvariable=var2,font=('Arial', 25),bg='#FFFFFF',fg='#000000').place(x=40,y=200)
alipaylogin=tk.PhotoImage(file='img/alipaylogin.png')
alipay_star=tk.Button(f_alipay,command=Alipay,image=alipaylogin).place(x=500,y=90)
#淘宝
f_taobao=second_level_class[1]
tb_var1=tk.StringVar()
tb_var2=tk.StringVar()
tb_var3=tk.StringVar()
tb_var4=tk.StringVar()
tb_var5=tk.StringVar()
tb_var6=tk.StringVar()
tb_var7=tk.StringVar()
tb_var1.set('123112，让我看看是谁来了')
tb_var2.set('想知sad道你的消费数据吗')
tb_var3.set('叫我一a声d小可爱，我就告诉你')
tb_var4.set('嘻vv据')
tb_var5.set('bb')
tb_var6.set('啊啊啊')

def testsittext():
    print('testsittext 调用了')
    tb_var1.set('11123112，让我看看是谁来了')
    tb_var2.set('11想知道你的消费数据吗')
    tb_var3.set('11叫我一声小可爱，我就告诉你')
    tb_var4.set('11嘻嘻嘻点击爬虫 查看详细数据')
    tb_var5.set('11嘻嘻嘻点击爬虫 查看详细数据')
    tb_var6.set('11嘻嘻嘻点击爬虫 查看详细数据')

# def TaoBaoxiangxishuju(r_class):
#     try :
#         tb_var1.set('213123123')
#         tb_var2.set('q1111')
#         tb_var3.set('叫我一声小可爱，我就告诉你')
#         tb_var4.set('嘻嘻嘻点击爬虫 查看详细数据')
#         tb_var5.set('嘻嘻嘻点击爬虫 查看详细数据')
#         tb_var6.set('嘻嘻嘻点击爬虫 查看详细数据')
#
#     except:
#         print('12121')
def taobaojiashuju():
    user_date.set('爬虫软件开始')
    time.sleep(8)
    dates = ['正在部署爬虫', '正在拉起登陆窗口', '正在处理登陆信息', '爬虫准备中', '正在爬虫', '正在获取数据标签', '正在获取数据','个人信息获取成功',
             '成功提取到地址信息','购物车数据已获取','浏览历史已获取','订单信息已获取','正在完善个人数据','正在提取标签','数据清洗中','数据准备完毕']
    for i in dates:
        user_date.set(i)
        time.sleep(6)
def time4():
    time.sleep(15)
    for i in range(10,83):
        time.sleep(0.7)
        change_schedule(i, 100)
def taobaoww():
        mm = askokcancel('提示', '操作之前，请打开您的taobao扫一扫功能，准备识别二维码')
        if mm == True:
            print('开始啦')
            for i in range(10):
                change_schedule(i, 100)
            taobaow()
        else:
            print('tuichul')
            pass
taobaoresult=[]
def taobaow():
    def str_taobao():
        print('str_taobao 调用了')
        taobaoresult=[['id'],['dizhi'],['gouwuc'],['qdqd'],['time']]
        testsittext()

    str_taobao()
    #     taobaoresturd = new_taobaos.go()
    #     print(new_taobao)
    #     f=open('taobao.txt','w')
    #     for i in taobaoresturd:
    #         f.write(i)
    #     f.close()
    #     for i in range(83, 100):
    #         time.sleep(0.3)
    #         change_schedule(i, 100)
    # for i in range(10):
    #     time.sleep(0.1)
    #     change_schedule(i, 100)
    # new_taobao = threading.Thread(target=str_taobao)
    # new_taobao.start()
    # t1 = threading.Thread(target=taobaojiashuju)
    # t2 = threading.Thread(target=time4)
    #
    # t1.start()
    # t2.start()

taoblogin=tk.PhotoImage(file='img/button_01.png')
taobmore=tk.PhotoImage(file='img/button_00.png')
taobao_star=tk.Button(f_taobao,command=taobaoww,image=taoblogin).place(x=470,y=390)
taobao_xiangxishuju=tk.Button(f_taobao,command=lambda :savepage(re_value,'taobao'),image=taobmore).place(x=600,y=390)
taobao_1=tk.Label(f_taobao,textvariable=tb_var1,font=('Arial', 15),bg='#FFFFFF',fg='#E95929').place(x=60,y=200)
taobao_2=tk.Label(f_taobao,textvariable=tb_var2,font=('Arial', 15),bg='#FFFFFF',fg='#E95929').place(x=60,y=250)
taobao_3=tk.Label(f_taobao,textvariable=tb_var3,font=('Arial', 15),bg='#FFFFFF',fg='#E95929').place(x=60,y=300)
taobao_4=tk.Label(f_taobao,textvariable=tb_var4,font=('Arial', 15),bg='#FFFFFF',fg='#E95929').place(x=60,y=350)
taobao_5=tk.Label(f_taobao,textvariable=tb_var5,font=('Arial', 15),bg='#FFFFFF',fg='#E95929').place(x=60,y=399)
taobao_6=tk.Label(f_taobao,textvariable=tb_var6,font=('Arial', 15),bg='#FFFFFF',fg='#E95929').place(x=60,y=459)

#bilibili
f_bilibili=second_level_class[2]
bb_var1=tk.StringVar()
bb_var2=tk.StringVar()
bb_var3=tk.StringVar()
bb_var4=tk.StringVar()
bb_var5=tk.StringVar()
bb_var1.set('欢迎来到哔哩看数据')
bb_var2.set('想知道你的爱好嘛')
bb_var3.set('要不要了解一下自己的浏览数据？')
bb_var4.set('兴趣爱好？')
bb_var5.set('点击开始，尝试一下！')

def bilibilixiangxishuju(resturt):
    bb_var1.set(str(resturt[0]))
    bb_var2.set(str(resturt[1]))
    bb_var3.set(str(resturt[2]))
    bb_var4.set(str(resturt[3]))
    bb_var5.set(str(resturt[4]))
def bilibilijiashuju():
    user_date.set('爬虫软件开始')
    time.sleep(8)
    dates = ['正在部署爬虫', '正在拉起登陆窗口', '正在处理登陆信息', '爬虫准备中', '正在爬虫', '正在获取数据标签', '正在获取数据','个人信息获取成功',
             '成功提取到地址信息','购物车数据已获取','浏览历史已获取','订单信息已获取','正在完善个人数据','正在提取标签','数据清洗中','数据准备完毕']
    for i in dates:
        user_date.set(i)
        time.sleep(6)
def time3():
    time.sleep(15)
    for i in range(10,83):
        change_schedule(i, 100)
bilibili_resurt=[]
def bilibiliw():
    def bil():
        mm = askokcancel('提示', '操作之前，请打开您的bilibil扫一扫功能，准备识别二维码')
        if mm == True:
            print('开始啦')
            for i in range(10):
                change_schedule(i, 100)
            str_bilibili()
        else:
            print('tuichul')
            pass
    def str_bilibili():
        new_bilibilis=BilBil()
        resturd=new_bilibilis.go()
        print(resturd)
        # global bilibili_resurt
        # bilibili_resurt=resturd
        # print(bilibili_resurt)
        #bilibilixiangxishuju(resturd)

    new_bilibili = threading.Thread(target=bil)
    new_bilibili.start()
    t1 = threading.Thread(target=bilibilijiashuju)
    t2 = threading.Thread(target=time3)
    t1.start()
    t2.start()

bilibillogin=tk.PhotoImage(file='img/bilibilbutton_01.png')
bilibilmore=tk.PhotoImage(file='img/bilibilbutton_00.png')
bilibil_star=tk.Button(f_bilibili,command=bilibiliw,image=bilibillogin).place(x=70,y=420)
bilibil_xiangxishuju=tk.Button(f_bilibili,command=lambda :savepage(bilibili_resurt,'bilibili'),image=bilibilmore).place(x=210,y=420)
bilibili_1=tk.Label(f_bilibili,textvariable=bb_var1,font=('Arial', 16),bg='#FFFFFF',fg='#000000').place(x=330,y=220)
bilibili_2=tk.Label(f_bilibili,textvariable=bb_var2,font=('Arial', 16),bg='#FFFFFF',fg='#000000').place(x=330,y=260)
bilibili_3=tk.Label(f_bilibili,textvariable=bb_var3,font=('Arial', 16),bg='#FFFFFF',fg='#000000').place(x=330,y=360)
bilibili_4=tk.Label(f_bilibili,textvariable=bb_var4,font=('Arial', 16),bg='#FFFFFF',fg='#000000').place(x=330,y=380)
bilibili_5=tk.Label(f_bilibili,textvariable=bb_var5,font=('Arial', 16),bg='#FFFFFF',fg='#000000').place(x=330,y=450)

#baidu
f_baidu=second_level_class[3]
bdyx_var1=tk.StringVar()
bdyx_var2=tk.StringVar()
bdyx_var3=tk.StringVar()
bdyx_var4=tk.StringVar()
bdyx_var5=tk.StringVar()
bdyx_var1.set('今天天气很不错')
bdyx_var2.set('今天有百度吗，想不想看看自己都浏览了哪些羞羞的信息？')
bdyx_var3.set('最热关键词，每天的热点，你都知道吗')
bdyx_var4.set('点击开始，给你送上专属称号')
bdyx_var5.set('快来试试吧')
def baiduxiangxishuju(er):
    bdyx_var1.set(er[0])
    bdyx_var2.set(er[0])
    bdyx_var3.set(er[0])
    bdyx_var4.set(er[0])
    bdyx_var5.set(er[0])
def baidujiashuju():
    user_date.set('爬虫软件开始')
    time.sleep(8)
    dates = ['正在部署爬虫', '正在拉起登陆窗口', '正在处理登陆信息', '爬虫准备中', '正在爬虫', '正在获取数据标签', '正在获取数据','个人信息获取成功',
             '成功提取到地址信息','购物车数据已获取','浏览历史已获取','订单信息已获取','正在完善个人数据','正在提取标签','数据清洗中','数据准备完毕']
    for i in dates:
        user_date.set(i)
        time.sleep(6)
def time4():
    time.sleep(15)
    for i in range(10,83):
        time.sleep(0.7)
        change_schedule(i, 100)
def baiduww():
    mm = askokcancel('提示', '操作之前，请打开您的baidu扫一扫功能，准备识别二维码')
    if mm == True:
        print('开始啦')
        for i in range(10):
            change_schedule(i, 100)
        baiduw()
    else:
        print('tuichul')
        pass
baiduresturd=[]
def baiduw():
    def str_baidu():
        new_baidus=BaiDu()
        resturd=new_baidus.go()
        print(resturd)
        baiduxiangxishuju(baiduresturd)
baidlogin=tk.PhotoImage(file='img/baid1.png')
baidumore=tk.PhotoImage(file='img/baid2.png')
baidu_star=tk.Button(f_baidu,command=baiduww,image=baidlogin).place(x=450,y=460)
baidu_xiangxishuju=tk.Button(f_baidu,command=lambda :savepage(baiduresturd,'baidu.txt'),image=baidumore).place(x=590,y=460)
baidu_1=tk.Label(f_baidu,textvariable=bdyx_var1,font=('Arial', 13),bg='#5E628A',fg='white').place(x=40,y=230)
baidu_2=tk.Label(f_baidu,textvariable=bdyx_var2,font=('Arial', 13),bg='#5E628A',fg='white').place(x=40,y=290)
baidu_3=tk.Label(f_baidu,textvariable=bdyx_var3,font=('Arial', 13),bg='#5E628A',fg='white').place(x=40,y=340)
baidu_4=tk.Label(f_baidu,textvariable=bdyx_var4,font=('Arial', 13),bg='#5E628A',fg='white').place(x=40,y=420)
baidu_5=tk.Label(f_baidu,textvariable=bdyx_var5,font=('Arial', 13),bg='#5E628A',fg='white').place(x=40,y=470)


#tuniu
f_tuniu=second_level_class[4]
tuniu_var1=tk.StringVar()
tuniu_var2=tk.StringVar()
tuniu_var3=tk.StringVar()
tuniu_var4=tk.StringVar()
tuniu_var5=tk.StringVar()
tuniu_var1.set('春风吹战鼓擂，新的一年往哪颓')
tuniu_var2.set('今天雨好大，好像不适合出去玩呢')
tuniu_var3.set('想知道你一年都去了哪些地方吗')
tuniu_var4.set('想知道偌大的中国都有哪些地方还没涉足吗')
tuniu_var5.set('点击这里 查看详细数据')
def tuniuxiangxishuju():
    tuniu_var1.set('吴昊，最近想去哪？')
    tuniu_var2.set('2020年7月5号是你最近一次出行，去了北京，玩的开心吗')
    tuniu_var3.set('你最近一直在浏览广州旅游的相关信息，广州最近天气不错')
    tuniu_var4.set('截止今天，中国56个省你已经去了12个呢 真不错')
    tuniu_var5.set('点击这里 查看详细数据')
def tuniujiashuju():
    user_date.set('爬虫软件开始')
    time.sleep(8)
    dates = ['正在部署爬虫', '正在拉起登陆窗口', '正在处理登陆信息', '爬虫准备中', '正在爬虫', '正在获取数据标签', '正在获取数据','个人信息获取成功',
             '成功提取到地址信息','购物车数据已获取','浏览历史已获取','订单信息已获取','正在完善个人数据','正在提取标签','数据清洗中','数据准备完毕']
    for i in dates:
        user_date.set(i)
        time.sleep(6)
def time5():
    time.sleep(15)
    for i in range(10,83):
        time.sleep(0.7)
        change_schedule(i, 100)
def tuniuw():
    def str_tuniu():
        new_tunius=TaoBao()
        tuniuxiangxishuju()
        print(type(new_tuniu))
        tuniuresturd = new_tunius.go()
        print(new_tuniu)
        f=open('tuniu.txt','w')
        for i in tuniuresturd:
            f.write(i)
        f.close()
        for i in range(83, 100):
            time.sleep(0.3)
            change_schedule(i, 100)
    for i in range(10):
        time.sleep(0.1)
        change_schedule(i, 100)
    new_tuniu = threading.Thread(target=str_tuniu)
    new_tuniu.start()
    t1 = threading.Thread(target=tuniujiashuju)
    t2 = threading.Thread(target=time5)

    t1.start()
    t2.start()
tuniu_star=tk.Button(f_tuniu,command=tuniuw,image=alipaylogin).place(x=500,y=90)
tuniu_xiangxishuju=tk.Button(f_tuniu,command=lambda :opendatas('tuniu.txt'),image=alipaylogin).place(x=500,y=390)
tuniu_1=tk.Label(f_tuniu,textvariable=tuniu_var1,font=('Arial', 25),bg='#5E628A',fg='white').place(x=40,y=120)
tuniu_2=tk.Label(f_tuniu,textvariable=tuniu_var2,font=('Arial', 25),bg='#5E628A',fg='white').place(x=40,y=180)
tuniu_3=tk.Label(f_tuniu,textvariable=tuniu_var3,font=('Arial', 25),bg='#5E628A',fg='white').place(x=40,y=240)
tuniu_4=tk.Label(f_tuniu,textvariable=tuniu_var4,font=('Arial', 25),bg='#5E628A',fg='white').place(x=40,y=300)
tuniu_5=tk.Label(f_tuniu,textvariable=tuniu_var5,font=('Arial', 25),bg='#5E628A',fg='white').place(x=40,y=360)


#qqemail
f_qqemail=second_level_class[5]
qqemail_var1=tk.StringVar()
qqemail_var2=tk.StringVar()
qqemail_var3=tk.StringVar()
qqemail_var4=tk.StringVar()
qqemail_var5=tk.StringVar()
qqemail_var1.set('2020 小B还没有找到工作，你呢')
qqemail_var2.set('我猜你是个程序员')
qqemail_var3.set('正在点燃箱子里的火')
qqemail_var4.set('正在活动指关节')
qqemail_var5.set('点击这里 查看详细数据')
def qqemailxiangxishuju(er):
    qqemail_var1.set(er[0][0])
    qqemail_var2.set(er[0][1])
    qqemail_var3.set(er[1][0])
    qqemail_var4.set(er[1][1])
    qqemail_var5.set(er[1][2])
def qqemailjiashuju():
    user_date.set('爬虫软件开始')
    time.sleep(8)
    dates = ['正在部署爬虫', '正在拉起登陆窗口', '正在处理登陆信息', '爬虫准备中', '正在爬虫', '正在获取数据标签', '正在获取数据','个人信息获取成功',
             '成功提取到地址信息','购物车数据已获取','浏览历史已获取','订单信息已获取','正在完善个人数据','正在提取标签','数据清洗中','数据准备完毕']
    for i in dates:
        user_date.set(i)
        time.sleep(6)
def time6():
    time.sleep(15)
    for i in range(10,83):
        time.sleep(0.7)
        change_schedule(i, 100)
resturds=[]
def qqemailw():
    def str_qqemail():
        new_qqemails=QQemail()
        resturd=new_qqemails.go()
        resturds=resturd
        print(resturd)
        qqemailxiangxishuju(resturd)

    new_qqemail = threading.Thread(target=str_qqemail)
    new_qqemail.start()
    t1 = threading.Thread(target=qqemailjiashuju)
    t2 = threading.Thread(target=time6)
    t1.start()
    t2.start()

qqemail_star=tk.Button(f_qqemail,command=qqemailw,image=alipaylogin).place(x=500,y=90)
qqemail_xiangxishuju=tk.Button(f_qqemail,command=lambda :savepage(resturds,'mail'),image=alipaylogin).place(x=500,y=390)
qqemail_1=tk.Label(f_qqemail,textvariable=qqemail_var1,font=('Arial', 25),bg='#5E628A',fg='white').place(x=40,y=120)
qqemail_2=tk.Label(f_qqemail,textvariable=qqemail_var2,font=('Arial', 25),bg='#5E628A',fg='white').place(x=40,y=180)
qqemail_3=tk.Label(f_qqemail,textvariable=qqemail_var3,font=('Arial', 25),bg='#5E628A',fg='white').place(x=40,y=240)
qqemail_4=tk.Label(f_qqemail,textvariable=qqemail_var4,font=('Arial', 25),bg='#5E628A',fg='white').place(x=40,y=300)
qqemail_5=tk.Label(f_qqemail,textvariable=qqemail_var5,font=('Arial', 25),bg='#5E628A',fg='white').place(x=40,y=360)


#wangyiyun
f_wangyiyun=second_level_class[6]
wangyiyun_var1=tk.StringVar()
wangyiyun_var2=tk.StringVar()
wangyiyun_var3=tk.StringVar()
wangyiyun_var4=tk.StringVar()
wangyiyun_var5=tk.StringVar()
wangyiyun_var1.set('欢迎，陌上花开')
wangyiyun_var2.set('好久不见，今天想听点什么')
wangyiyun_var3.set('我能找到你最喜欢的音乐吗')
wangyiyun_var4.set('关于音乐我们准备了这些')
wangyiyun_var5.set('点击这里 查看详细数据')
def oppppp():
    playsound('1.mp3')
def musicopen(path):
    musicop = threading.Thread(target=oppppp)
    musicop.start()

def wangyiyunxiangxishuju(a):
    wangyiyun_var1.set(a[0][0])
    wangyiyun_var2.set(a[0][2])
    wangyiyun_var3.set(a[0][1])
    wangyiyun_var4.set(a[0][3])
    wangyiyun_var5.set(a[0][4])

def wangyiyunkais():
    mm = askokcancel('提示', '操作之前，请打开您的网易云扫一扫功能，准备识别二维码')
    if mm==True:
        print('开始啦')
        wangyiyunw()
    else:
        print('tuichul')
        pass
def wangyiyunjiashuju():
    user_date.set('爬虫软件开始')
    time.sleep(8)
    dates = ['正在部署爬虫', '正在拉起登陆窗口', '正在处理登陆信息', '爬虫准备中', '正在爬虫', '正在获取数据标签', '正在获取数据','个人信息获取成功',
             '成功提取到地址信息','购物车数据已获取','浏览历史已获取','订单信息已获取','正在完善个人数据','正在提取标签','数据清洗中','数据准备完毕']
    for i in dates:
        user_date.set(i)
        time.sleep(6)
def time7():
    time.sleep(15)
    for i in range(10,83):
        time.sleep(0.7)
        change_schedule(i, 100)
wwwww=[]
def wangyiyunw():
    def str_wangyiyun():
        new_wangyiyuns=go()
        print(new_wangyiyuns)

    str_wangyiyun()
wangyiyun_open=tk.Button(f_wangyiyun,command=lambda :musicopen('1.mp3'),text='播放').place(x=500,y=100)
wangyiyun_star=tk.Button(f_wangyiyun,command=wangyiyunkais,text='登陆').place(x=500,y=470)
wangyiyun_xiangxishuju=tk.Button(f_wangyiyun,command=lambda :savepage(wwwww,'wangyiyun'),text='下载').place(x=600,y=470)
wangyiyun_1=tk.Label(f_wangyiyun,textvariable=wangyiyun_var1,font=('Arial', 13),bg='#FFFFFF',fg='#000000').place(x=40,y=250)
wangyiyun_2=tk.Label(f_wangyiyun,textvariable=wangyiyun_var2,font=('Arial', 13),bg='#FFFFFF',fg='#000000').place(x=40,y=295)
wangyiyun_3=tk.Label(f_wangyiyun,textvariable=wangyiyun_var3,font=('Arial', 13),bg='#FFFFFF',fg='#000000').place(x=40,y=335)
wangyiyun_4=tk.Label(f_wangyiyun,textvariable=wangyiyun_var4,font=('Arial', 13),bg='#FFFFFF',fg='#000000').place(x=40,y=380)
wangyiyun_5=tk.Label(f_wangyiyun,textvariable=wangyiyun_var5,font=('Arial', 13),bg='#FFFFFF',fg='#000000').place(x=40,y=423)


#meituan
f_meituan=second_level_class[7]
meituan_var1=tk.StringVar()
meituan_var2=tk.StringVar()
meituan_var3=tk.StringVar()
meituan_var4=tk.StringVar()
meituan_var5=tk.StringVar()
meituan_var6=tk.StringVar()
meituan_var1.set('好饿好饿好饿')
meituan_var2.set('今天还能吃点啥')
meituan_var3.set('用了这么久的美团，要不要看看自己的特别关心？')
meituan_var4.set('想吃小龙虾')
meituan_var5.set('点击试试看')
meituan_var6.set('点击试试看')
def meituanxiangxishuju():
    meituan_var1.set('吴昊，很高兴遇到你')
    meituan_var2.set('你最喜欢的一家店是，重庆鸡公煲')
    meituan_var3.set('平均6天点一次外卖，果然是良家煮男')
    meituan_var4.set('最晚一次消费，0：34 深夜食堂 啤酒小龙虾')
    meituan_var5.set('点击这里 查看详细数据')
def meituanjiashuju():
    user_date.set('爬虫软件开始')
    time.sleep(8)
    dates = ['正在部署爬虫', '正在拉起登陆窗口', '正在处理登陆信息', '爬虫准备中', '正在爬虫', '正在获取数据标签', '正在获取数据','个人信息获取成功',
             '成功提取到地址信息','购物车数据已获取','浏览历史已获取','订单信息已获取','正在完善个人数据','正在提取标签','数据清洗中','数据准备完毕']
    for i in dates:
        user_date.set(i)
        time.sleep(6)
def time8():
    time.sleep(15)
    for i in range(10,83):
        time.sleep(0.7)
        change_schedule(i, 100)
def meituanw():
    def str_meituan():
        new_meituans=MeiTuan()
        resturd=new_meituans.go()
        print(resturd)
    str_meituan()
    #     print(type(new_meituan))
    #     # meituanresturd = new_meituans.go()
    #     print(new_meituan)
    #     f=open('meituan.txt','w')
    #     # for i in meituanresturd:
    #     #     f.write(i)
    #     f.close()
    #     for i in range(83, 100):
    #         time.sleep(0.3)
    #         change_schedule(i, 100)
    # for i in range(10):
    #     time.sleep(0.1)
    #     change_schedule(i, 100)
    # new_meituan = threading.Thread(target=str_meituan)
    # new_meituan.start()
    # t1 = threading.Thread(target=meituanjiashuju)
    # t2 = threading.Thread(target=time8)
    #
    # t1.start()
    # t2.start()
meituan_l1=tk.Label(f_meituan,text='用户名').place(x=500,y=400)
meituan_l2=tk.Label(f_meituan,text='密码').place(x=500,y=430)
meituan_e1=tk.Entry(f_meituan,show=None)
meituan_e1.place(x=550,y=400)
meituan_e2=tk.Entry(f_meituan,show='*')
meituan_e2.place(x=550,y=430)
meituan_star=tk.Button(f_meituan,command=meituanw,text='查询').place(x=560,y=470)
meituan_xiangxishuju=tk.Button(f_meituan,command=lambda :opendatas('xuexinw.txt'),text='下载').place(x=660,y=470)
meituan_1=tk.Label(f_meituan,textvariable=meituan_var1,font=('Arial', 15),bg='#FFFFFF',fg='#000000').place(x=70,y=215)
meituan_2=tk.Label(f_meituan,textvariable=meituan_var2,font=('Arial', 15),bg='#FFFFFF',fg='#000000').place(x=70,y=265)
meituan_3=tk.Label(f_meituan,textvariable=meituan_var3,font=('Arial', 15),bg='#FFFFFF',fg='#000000').place(x=70,y=315)
meituan_4=tk.Label(f_meituan,textvariable=meituan_var4,font=('Arial', 15),bg='#FFFFFF',fg='#000000').place(x=70,y=365)
meituan_5=tk.Label(f_meituan,textvariable=meituan_var5,font=('Arial', 15),bg='#FFFFFF',fg='#000000').place(x=70,y=420)
meituan_6=tk.Label(f_meituan,textvariable=meituan_var6,font=('Arial', 15),bg='#FFFFFF',fg='#000000').place(x=70,y=470)


#xuexinw
f_xuexinw=second_level_class[8]
xx_var1=tk.StringVar()
xx_var2=tk.StringVar()
xx_var3=tk.StringVar()
xx_var4=tk.StringVar()
xx_var5=tk.StringVar()
xx_var6=tk.StringVar()
xx_var7=tk.StringVar()
xx_var8=tk.StringVar()
xx_var9=tk.StringVar()
xx_var10=tk.StringVar()
xx_var11=tk.StringVar()
xx_var12=tk.StringVar()


# im1 = Image.open('/Users/jiguang-macpro/PycharmProjects/untitled1/Allen/user_info.jpg') #支持相对或绝对路径，支持多种格式
# im2=ImageTk.PhotoImage(im1)
xuex=[]
def xuexinww():
    def str_xuexinw():
        user_date.set('爬虫软件开始')
        for i in range(10):
            change_schedule(i, 100)
        name=xuexinw_e1.get()
        password=xuexinw_e2.get()
        new_xuexinws=Login(name,password)
        resturt=new_xuexinws.xx()
        xuex.append(resturt)
        print(resturt)
        for i in range(0, 100):
            change_schedule(i, 100)

        canvas = tk.Canvas(f_xuexinw, width=200, height=267)
        canvas.create_image(0,0,anchor='nw',image=im2)
        canvas.place(x=540, y=110)

        xx_var1.set(resturt[0])
        xx_var2.set(resturt[1])
        xx_var3.set(resturt[2])
        xx_var4.set(resturt[3])
        xx_var5.set(resturt[4])
        xx_var6.set(resturt[5])
        xx_var7.set(resturt[6])
        xx_var8.set(resturt[7])
        xx_var9.set(resturt[8])
        xx_var10.set(resturt[9])
        xx_var11.set(resturt[10])
        xx_var12.set(resturt[11])
    str_xuexinw()

xuexinw_l1=tk.Label(f_xuexinw,text='用户名').place(x=500,y=400)
xuexinw_l2=tk.Label(f_xuexinw,text='密码').place(x=500,y=430)
xuexinw_e1=tk.Entry(f_xuexinw,show=None)
xuexinw_e1.place(x=550,y=400)
xuexinw_e2=tk.Entry(f_xuexinw,show='*')
xuexinw_e2.place(x=550,y=430)
xuexinw_star=tk.Button(f_xuexinw,command=xuexinww,text='查询').place(x=560,y=470)
xuexinw_xiangxishuju=tk.Button(f_xuexinw,command=lambda :savepage(xuex,'xuexinw'),text='下载').place(x=660,y=470)
xuexinw_1=tk.Label(f_xuexinw,textvariable=xx_var1,font=('Arial', 13),bg='#FFFFFF',fg='#000000').place(x=70,y=190)
xuexinw_2=tk.Label(f_xuexinw,textvariable=xx_var2,font=('Arial', 13),bg='#FFFFFF',fg='#000000').place(x=70,y=242)
xuexinw_3=tk.Label(f_xuexinw,textvariable=xx_var3,font=('Arial', 13),bg='#FFFFFF',fg='#000000').place(x=70,y=295)
xuexinw_4=tk.Label(f_xuexinw,textvariable=xx_var4,font=('Arial', 13),bg='#FFFFFF',fg='#000000').place(x=70,y=350)
xuexinw_5=tk.Label(f_xuexinw,textvariable=xx_var5,font=('Arial', 13),bg='#FFFFFF',fg='#000000').place(x=70,y=399)
xuexinw_6=tk.Label(f_xuexinw,textvariable=xx_var6,font=('Arial', 13),bg='#FFFFFF',fg='#000000').place(x=70,y=453)
xuexinw_7=tk.Label(f_xuexinw,textvariable=xx_var7,font=('Arial', 13),bg='#FFFFFF',fg='#000000').place(x=370,y=190)
xuexinw_8=tk.Label(f_xuexinw,textvariable=xx_var8,font=('Arial', 13),bg='#FFFFFF',fg='#000000').place(x=370,y=242)
xuexinw_9=tk.Label(f_xuexinw,textvariable=xx_var9,font=('Arial', 13),bg='#FFFFFF',fg='#000000').place(x=370,y=295)
xuexinw_10=tk.Label(f_xuexinw,textvariable=xx_var10,font=('Arial', 13),bg='#FFFFFF',fg='#000000').place(x=370,y=350)
xuexinw_11=tk.Label(f_xuexinw,textvariable=xx_var11,font=('Arial', 13),bg='#FFFFFF',fg='#000000').place(x=370,y=399)
xuexinw_12=tk.Label(f_xuexinw,textvariable=xx_var12,font=('Arial', 13),bg='#FFFFFF',fg='#000000').place(x=370,y=453)


#jingdong
f_jingdong=second_level_class[9]
tb_var1=tk.StringVar()
tb_var2=tk.StringVar()
tb_var3=tk.StringVar()
tb_var4=tk.StringVar()
tb_var5=tk.StringVar()

def jingdongxiangxishuju():
    tb_var1.set('吴昊，很高兴遇到你')
    tb_var2.set('2020年7月5号是你最近一次登陆淘宝，有找到喜欢的东西吗')
    tb_var3.set('2019年你共浏览商品13632次，下单120次，获得称号剁手狂魔')
    tb_var4.set('2019年6月 你给***购买了情人节礼物，她一定很幸福吧')
    tb_var5.set('点击这里 查看详细数据')
def jingdongjiashuju():
    user_date.set('爬虫软件开始')
    time.sleep(8)
    dates = ['正在部署爬虫', '正在拉起登陆窗口', '正在处理登陆信息', '爬虫准备中', '正在爬虫', '正在获取数据标签', '正在获取数据','个人信息获取成功',
             '成功提取到地址信息','购物车数据已获取','浏览历史已获取','订单信息已获取','正在完善个人数据','正在提取标签','数据清洗中','数据准备完毕']
    for i in dates:
        user_date.set(i)
        time.sleep(6)
def time10():
    time.sleep(15)
    for i in range(10,83):
        time.sleep(0.7)
        change_schedule(i, 100)
def jingdongw():
    def str_jingdong():
        new_jingdongs=TaoBao()
        jingdongxiangxishuju()
        print(type(new_jingdong))
        jingdongresturd = new_jingdongs.go()
        print(new_jingdong)
        f=open('jingdong.txt','w')
        for i in jingdongresturd:
            f.write(i)
        f.close()
        for i in range(83, 100):
            time.sleep(0.3)
            change_schedule(i, 100)
    for i in range(10):
        time.sleep(0.1)
        change_schedule(i, 100)
    new_jingdong = threading.Thread(target=str_jingdong)
    new_jingdong.start()
    t1 = threading.Thread(target=jingdongjiashuju)
    t2 = threading.Thread(target=time10)

    t1.start()
    t2.start()
jingdong_star=tk.Button(f_jingdong,command=jingdongw,image=alipaylogin).place(x=500,y=90)
jingdong_xiangxishuju=tk.Button(f_jingdong,command=lambda :opendatas('jingdong.txt'),image=alipaylogin).place(x=500,y=390)
jingdong_1=tk.Label(f_jingdong,textvariable=tb_var1,font=('Arial', 25),bg='#5E628A',fg='white').place(x=40,y=120)
jingdong_2=tk.Label(f_jingdong,textvariable=tb_var2,font=('Arial', 25),bg='#5E628A',fg='white').place(x=40,y=180)
jingdong_3=tk.Label(f_jingdong,textvariable=tb_var3,font=('Arial', 25),bg='#5E628A',fg='white').place(x=40,y=240)
jingdong_4=tk.Label(f_jingdong,textvariable=tb_var4,font=('Arial', 25),bg='#5E628A',fg='white').place(x=40,y=300)
jingdong_5=tk.Label(f_jingdong,textvariable=tb_var5,font=('Arial', 25),bg='#5E628A',fg='white').place(x=40,y=360)
#首页
shouyeimg=tk.PhotoImage(file='img/maddol.png')
shouye_img_sit=tk.Label(second_level_class[13],image=shouyeimg).place(x=0,y=0)
guanyuwomen_img_sit=tk.Label(second_level_class[10],image=shouyeimg).place(x=0,y=0)
#关于我们
f_guany=second_level_class[10]
shouyeimg=tk.PhotoImage(file='img/11.png')
guanyu_img_sit=tk.Label(f_guany,image=shouyeimg).place(x=0,y=0)
#人物画像
f_huax=second_level_class[11]
huaxiangimg=tk.PhotoImage(file='img/12.png')
huaxiang_img_sit=tk.Label(f_huax,image=huaxiangimg).place(x=0,y=0)


root.mainloop()