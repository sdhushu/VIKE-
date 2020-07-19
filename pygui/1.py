from PIL import Image

img = Image.open('adress.png')
box = (300, 200, 750, 580)
img = img.crop(box)
# 保存到本地
img.save('adress1.png')
img.show()