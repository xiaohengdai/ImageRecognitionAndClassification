from colorsys import rgb_to_hsv

import cv2  # 导入OpenCV库
import numpy as np
from sklearn.cluster import KMeans



def centroid_histogram(clt):
    # print('np.unique(clt.labels_):',np.unique(clt.labels_))
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins=numLabels)  # a是待统计数据的数组；,bins指定统计的区间个数；
    # print('numLabels:', numLabels)
    # print('hist2:',hist)
    hist = hist.astype("float")
    # print('hist0:', hist)
    hist /= hist.sum()
    # print('hist1:',hist)
    return hist

def to_hsv(color):
    """ converts color tuples to floats and then to hsv """
    return rgb_to_hsv(*[x / 255.0 for x in color])  # rgb_to_hsv wants floats!

def plot_colors(hist, centroids):
    bar = np.zeros((50, 300, 3), dtype="uint8")
    startX = 0
    percent1 = []
    color1 = []

    for (percent, color) in zip(hist, centroids):  # 从参数中的多个迭代器取元素组合成一个新的迭代器
        endX = startX + (percent * 300)
        cv2.rectangle(bar, (int(startX), 0), (int(endX), 50),
                      color.astype("uint8").tolist(), -1)
        startX = endX
        percent1.append(percent)
        color1.append(color)
        # print('percent:',percent)
        # print('color:',color)

    return bar, percent1, color1

def get_main_tonal_rgb_value(image_path, clusters):
    """

    :param image_path:图片的路径
    :param clusters:聚类后的颜色种类
    :return:得到最多聚类颜色的RGB值
    """
    image = cv2.imdecode(np.fromfile(image_path, dtype=np.uint8), -1)# opencv默认的彩色图像的颜色空间是BGR
    #image = cv2.imread(image_path)  # opencv默认的彩色图像的颜色空间是BGR
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = image.reshape((image.shape[0] * image.shape[1], 3))
    clt = KMeans(n_clusters=clusters)
    print(clt)
    print(image)
    clt.fit(image)
    hist = centroid_histogram(clt)
    bar, percent1, color1 = plot_colors(hist, clt.cluster_centers_)
    print('percent1:    ', percent1)
    print('color1:  ', color1)
    color1_0_int = color1[0].astype('int64')
    print('color1_0_in:', color1_0_int)  # 最后的返回值
    return color1_0_int


def color_dist(c1, c2):
    """ returns the squared euklidian distance between two color vectors in hsv space """
    return sum((a - b) ** 2 for a, b in zip(to_hsv(c1), to_hsv(c2)))

def min_color_diff(color_to_match, colors):
    """

    :param color_to_match:指定颜色的RGB值
    :param colors:待识别颜色库里各颜色的RGB值
    :return:在颜色库中最接近指定颜色RGB值的颜色
    """
    """ returns the `(distance, color_name)` with the minimal distance to `colors`"""
    return min(  # overal best is the best match to any color:
        (color_dist(color_to_match, test), colors[test])  # (distance to `test` color, color name)
        for test in colors)


def get_main_tonal_value(image_path, clusters):
    colors = dict((
        ((196, 2, 51), "RED"),
        ((255, 165, 0), "ORANGE"),
        ((255, 205, 0), "YELLOW"),
        ((0, 128, 0), "GREEN"),
        ((0, 0, 255), "BLUE"),
        ((127, 0, 255), "VIOLET"),
        ((0, 0, 0), "BLACK"),
        ((255, 255, 255), "WHITE"),))
    main_tonal_color_value = min_color_diff(get_main_tonal_rgb_value(image_path, clusters), colors)
    print("main_tonal_color_value:",main_tonal_color_value)
    return main_tonal_color_value[1]

image_path="/Users/xiaoheng/Downloads/meituan/kl_depth_performance_android/webview-tools/workspace/loadPics/iOS_支付页/2.png"
clusters=1

main_tonal_color = get_main_tonal_value(image_path, clusters)