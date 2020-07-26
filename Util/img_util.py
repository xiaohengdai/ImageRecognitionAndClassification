# *_*coding:utf-8 *_*

import numpy as np
import cv2

# 得到图片分辨率
def get_image_resolve(discern_img_path=''):
    """
    :param discern_img_path:获取图片的路径
    :return:返回长和宽
    """
    img = cv2.imdecode(np.fromfile(discern_img_path, dtype=np.uint8), -1)
    sp = img.shape
    height = sp[0]  # height(rows) of image
    width = sp[1]  # width(colums) of image
    channel = sp[2]  # the pixels value is made up of three primary colors
    print('图片的长height:  ', height)
    print('图片的宽width:   ', width)
    print('channel: ', channel)
    return height, width

# 读取图片 & 返回图片对象
def read_img(src):
    """
    :param src:图片的路径
    :return:返回图片数据
    """
    return cv2.imdecode(np.fromfile(src, dtype=np.uint8), 100)


