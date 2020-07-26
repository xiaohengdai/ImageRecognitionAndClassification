# *_*coding:utf-8 *_*

import cv2


# 图像模糊
from Util.img_util import read_img

#为了实现对图像噪声的消除，增强图像的效果
def image_blur(img_src, img_dst):
    """

    :param img_src:传入图片的路径
    :param img_dst:模糊化后图片的路径
    :return:
    """
    src = read_img(img_src)
    dst = cv2.blur(src, (15, 1))  #均值滤波
    # cv2.imshow("blur_demo", dst)
    cv2.imwrite(img_dst, dst)
