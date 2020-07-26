# *_*coding:utf-8 *_*

import cv2
import numpy as np
from Util.img_util import read_img

#图像腐蚀,#腐蚀类似 '领域被蚕食' ,将图像中的高亮区域或白色部分进行缩减细化,其运行结果图比原图的高亮区域更小.
def image_corrosion(img_src,img_dst):
    src = read_img(img_src)
    ## b.设置卷积核5*5
    kernel = np.ones((5, 5), np.uint8)
    ## c.图像的腐蚀，默认迭代次数
    erosion = cv2.erode(src, kernel)
    #腐蚀后，图像明显变黑很多
    cv2.imwrite(img_dst, erosion)