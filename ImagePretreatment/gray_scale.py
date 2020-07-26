# *_*coding:utf-8 *_*
import cv2
from Util.img_util import read_img


# 对图片进行灰度
def gray_scale(img_src_path, img_dst_path):
    """
    :param img_src_path:图片的源路径
    :param img_dst_path:灰度化的图片路径
    :return:img_dst_path
    """
    img = read_img(img_src_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#RGB颜色空间以R(Red:红)、G(Green:绿)、B(Blue:蓝)
    cv2.imwrite(img_dst_path, gray)
    return img_dst_path
