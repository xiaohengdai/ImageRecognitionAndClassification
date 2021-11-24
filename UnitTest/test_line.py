import cv2
import numpy as np
# 使用霍夫直线变换做直线检测，前提条件：边缘检测已经完成




# 标准霍夫线变换
# def line_detection_demo(image):
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     edges = cv2.Canny(gray, 50, 150, apertureSize=3)
#     lines = cv2.HoughLines(edges, 1, np.pi/180, 200)  # 函数将通过步长为1的半径和步长为π/180的角来搜索所有可能的直线
#     for line in lines:
#         rho, theta = line[0]  # line[0]存储的是点到直线的极径和极角，其中极角是弧度表示的
#         a = np.cos(theta)   # theta是弧度
#         b = np.sin(theta)
#         x0 = a * rho
#         y0 = b * rho
#         x1 = int(x0 + 1000 * (-b))  # 直线起点横坐标
#         y1 = int(y0 + 1000 * (a))   # 直线起点纵坐标
#         x2 = int(x0 - 1000 * (-b))  # 直线终点横坐标
#         y2 = int(y0 - 1000 * (a))   # 直线终点纵坐标
#         cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
#     cv2.imshow("image_lines", image)


# 统计概率霍夫线变换
def line_detect_possible_demo(image):
    #这个识别比较准
    #可以指定待识别直线的区域，判断待识别区域中是否存在这条直线
    gray = cv2.cvtColor(image, cv2.COLOR_BGRA2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)  ## 使用霍夫直线变换做直线检测，前提条件：边缘检测已经完成
    # 函数将通过步长为1的半径和步长为π/180的角来搜索所有可能的直线
    lines = cv2.HoughLinesP(image=edges, rho=1, theta=np.pi / 180,threshold= 100, minLineLength=50, maxLineGap=10)
    # image参数表示边缘检测的输出图像，该图像为单通道8位二进制图像。
    # rho参数表示参数极径 r 以像素值为单位的分辨率，这里一般使用 1 像素。
    #theta参数表示参数极角 \theta 以弧度为单位的分辨率，这里使用 1度。
    #threshold参数表示检测一条直线所需最少的曲线交点
    #lines参数表示储存着检测到的直线的参数对 (x_{start}, y_{start}, x_{end}, y_{end}) 的容器，也就是线段两个端点的坐标。
    #minLineLength参数表示能组成一条直线的最少点的数量，点数量不足的直线将被抛弃。
    #maxLineGap参数表示能被认为在一条直线上的亮点的最大距离。

    for line in lines:
        print("line[0]:",line[0])
        x1, y1, x2, y2 = line[0]
        cv2.line(image, (x1, y1), (x2, y2), (255,0,0), 2)
    cv2.imshow("line_detect_possible_demo", image)


if __name__ == "__main__":

    img = cv2.imread("/Users/xh/Downloads/ks/follw_time_cost/test_straight_line/irs-4b5d35d4d24bb2a56081695bba72f6bf.mp4.mp4/00270.jpg")
    cv2.namedWindow("input image", cv2.WINDOW_AUTOSIZE)
    cv2.imshow("input image", img)
    line_detect_possible_demo(img)
    # line_detection_demo(img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


