# *_*coding:utf-8 *_*

import cv2
import numpy as np

#局部阈值
from Util.img_util import read_img


# 局部自适应二值化采用了分块，效果比全局二值化只采用了一种threshold这种，效果要好很多
def binary_local_threshold(img_src,img_dst):
    """

     :param img_src:传入图片的路径
     :param img_dst:模糊化后图片的路径
     :return:
     """
    src = read_img(img_src)
    gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)  #把输入图像灰度化
    #自适应阈值化能够根据图像不同区域亮度分布，改变阈值
    binary =  cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 25, 10)
    # cv2.namedWindow("binary1", cv2.WINDOW_NORMAL)
    # cv2.imshow("binary1", binary)
    cv2.imwrite(img_dst, binary)

