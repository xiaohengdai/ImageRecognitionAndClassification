# *_*coding:utf-8 *_*
import glob
import os

from PIL import Image

# 批量改变图片分辨率

# img_path = glob.glob("D:/转转/picture_set/ios_update/750_1334/*.jpg")
img_path = glob.glob("/Users/xiaoheng/Downloads/个人照片/老婆.jpeg")
# img_path ="/Users/xiaoheng/Downloads/个人照片/老婆.jpeg"
print('img_path:    ',img_path)
window_x=1080
window_y=1920

path_save = "/Users/xiaoheng/Downloads/个人照片/"+str(window_x)+'_'+str(window_y)
if not os.path.exists(path_save):
    os.makedirs(path_save)

i=0
for file in img_path:
    i=i+1
    name = os.path.join(path_save, str(i)+'_('+str(window_x)+','+str(window_y)+').jpg')
    name=name.replace('\\','/')
    print('name:    ',name)
    im = Image.open(file)
    print('im.size: ',im.size)
    reim=im.resize((window_x,window_y))  #返回一个新的Image对象
    print(reim.format, reim.size, reim.mode)
    reim.save(name,'JPEG')

    #cv2.imwrite(name,im)




# 一张图片生成不同分辨率的图片集，在同一个目录下

