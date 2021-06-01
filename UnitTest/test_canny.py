"""
cv2.Canny(image,            # 输入原图（必须为单通道图）
          threshold1,
          threshold2,       # 较大的阈值2用于检测图像中明显的边缘
          [, edges[,
          apertureSize[,    # apertureSize：Sobel算子的大小
          L2gradient ]]])   # 参数(布尔值)：
                              true： 使用更精确的L2范数进行计算（即两个方向的倒数的平方和再开放），
                              false：使用L1范数（直接将两个方向导数的绝对值相加）。
"""
#可以识别出当前页面主要的轮廓
#参考文章：
# 1、OpenCV—python 边缘检测（Canny）：https://blog.csdn.net/wsp_1138886114/article/details/82935839

import os

import cv2
import numpy as np

root_path=os.path.abspath(os.path.join(os.getcwd(),".."))
print("root_path:",root_path)
pic_path=os.path.join(root_path,"SamplePicSet","7.jpg")
print("pic_path:",pic_path)
original_img = cv2.imread(pic_path, 0)

# canny(): 边缘检测
img1 = cv2.GaussianBlur(original_img, (3, 3), 0)
canny = cv2.Canny(img1, 50, 150)

# 形态学：边缘检测
_, Thr_img = cv2.threshold(original_img, 210, 255, cv2.THRESH_BINARY)  # 设定红色通道阈值210（阈值影响梯度运算效果）
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))  # 定义矩形结构元素
gradient = cv2.morphologyEx(Thr_img, cv2.MORPH_GRADIENT, kernel)  # 梯度
print("original_img:",original_img)
print("gradient:",gradient)
print("canny:",canny)

# cv2.imshow("original_img", original_img)
# cv2.imshow("gradient", gradient)
# cv2.imshow('Canny', canny)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()

