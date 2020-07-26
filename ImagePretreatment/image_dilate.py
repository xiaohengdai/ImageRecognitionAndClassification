# *_*coding:utf-8 *_*

import cv2
import numpy as np
from Util.img_util import read_img

#图像膨胀
def image_dilate(img_src,img_dst):
    #膨胀类似与 '领域扩张' ,将图像的高亮区域或白色部分进行扩张,其运行结果图比原图的高亮区域更大
    src = read_img(img_src)
    ## 设置卷积核5*5
    kernel = np.ones((5, 5), np.uint8)
    ## 图像的腐蚀，默认迭代次数
    erosion = cv2.erode(src, kernel)
    ## 图像的膨胀
    dst = cv2.dilate(erosion, kernel)  #在图像上进行从左到右，从上到下的平移，如果方框中存在白色，那么这个方框内所有的颜色都是白色
    cv2.imwrite(img_dst, dst)