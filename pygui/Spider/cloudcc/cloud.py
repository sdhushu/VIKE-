from wordcloud import WordCloud

from PIL import Image

import jieba
def cloudcc(text):
        newtext=  ' '.join(jieba.cut(text, cut_all = False))
        wc = WordCloud(
                scale=2,
                max_font_size=100,  #最大字号
                background_color='white' , #设置背景颜色
            #中文请打开注释 并配置字体完整路径
                # font_path = '01.ttf',
                )
        def sitcloud(text):
                wc.generate(text)  # 从文本生成wordcloud
                wc.to_file('标签云效果图.png')  # 储存图像
                f=Image.open('标签云效果图.png')
        sitcloud(newtext)