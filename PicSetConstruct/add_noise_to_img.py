# *_*coding:utf-8 *_*

import numpy as np
import random
import cv2

from Util.img_util import read_img


def sp_noise(image,prob):
    '''
    添加椒盐噪声
    prob:噪声比例，比例越小，表示噪声越小
    '''
    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    cv2.imwrite("D:/pythonProject/ImageRecognitionAndClassification/UnitTest/ImgReco/small_tool_7.png", output)
    return output


def gasuss_noise(image, mean=0, var=0.001):
    '''
        添加高斯噪声
        mean : 均值
        var : 方差
    '''
    image = np.array(image/255, dtype=float)
    noise = np.random.normal(mean, var ** 0.5, image.shape)
    out = image + noise
    if out.min() < 0:
        low_clip = -1.
    else:
        low_clip = 0.
    out = np.clip(out, low_clip, 1.0)
    out = np.uint8(out*255)
    cv2.imwrite("D:/pythonProject/ImageRecognitionAndClassification/UnitTest/ImgReco/small_tool_6.png", out)
    return out

img_path="D:/pythonProject/ImageRecognitionAndClassification/UnitTest/ImgReco/small_tool_2.png"

#gasuss_noise(image=read_img(img_path))

sp_noise(image=read_img(img_path),prob=0.1)