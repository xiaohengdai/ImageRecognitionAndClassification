# *_*coding:utf-8 *_*
from PIL import Image, ImageDraw

from Util.img_util import get_image_resolve

pic_path="D:/pythonProject/ImageRecognitionAndClassification/UnitTest/ImgReco/small_tool_1_temp.png"
l_x0=0.3 #左上角的x
l_y0=0.3 #左上角的y
l_x1=0.5 #右下角的x
l_y1=0.5 #右下角的y

window_y,window_x=get_image_resolve(pic_path)
print('window_y:    ',window_y)
print('window_x:    ',window_x)

im = Image.open(pic_path)
outdraw = ImageDraw.Draw(im)
outdraw.rectangle((l_x0*window_x, l_y0*window_y, l_x1*window_x, l_y1*window_y), outline='red')
im.save(pic_path)

outdraw.text()