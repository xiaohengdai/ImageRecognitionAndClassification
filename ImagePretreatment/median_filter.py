import cv2
import numpy as np

#椒盐噪点（使用中值滤波去除）
def salt(img, n):
    for k in range(n):
        i = int(np.random.random() * img.shape[1])
        j = int(np.random.random() * img.shape[0])
        if img.ndim == 2:
            img[j,i] = 255
        elif img.ndim == 3:
            img[j,i,0]= 255
            img[j,i,1]= 255
            img[j,i,2]= 255
        return img

img = cv2.imread("D:/pythonProject/ImageRecognitionAndClassification/UnitTest/ImgReco/small_tool.png",cv2.IMREAD_GRAYSCALE) #先灰度化
result = salt(img, 500) #对图片加上椒盐噪声
median = cv2.medianBlur(result, 5)  #用中值滤波去除椒盐噪声
cv2.imshow("original_img", img)
cv2.imshow("Salt", result)
cv2.imshow("Median", median)
cv2.waitKey(0)
cv2.destroyWindow()
