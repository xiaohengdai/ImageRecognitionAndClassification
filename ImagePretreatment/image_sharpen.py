# *_*coding:utf-8 *_*

# 图像 锐化

import cv2
import numpy as np

from Util.img_util import read_img

# 图像锐化，凸显出图片边缘
def image_sharpen(img_src,img_dst):



    """

    :param img_src:传入图片的路径
    :param img_dst:模糊化后图片的路径
    :return:
    """
    image = read_img(img_src)
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32)  # 锐化
    dst = cv2.filter2D(image, -1, kernel=kernel)  #滤波器
    cv2.imwrite(img_dst, dst)



