# *_*coding:utf-8 *_*
import os

from PIL import Image, ImageDraw
from airtest.core.cv import Template
from ImageRecognition.constant import *
# from Util.get_yaml_config_info import get_yaml_config_info
# from Util.img_util import *
# from Util.log import Logger
import numpy as np
import cv2
root_path=(os.path.abspath(os.path.dirname(__file__)) + os.path.sep).replace('\\', '/')
current_path=os.path.abspath(os.path.dirname(__file__)).replace('\\', '/')
pics_set_dir=os.path.join(current_path,'ReferenceImage').replace('\\', '/')
print('pics_set_dir:    ',pics_set_dir)




class MatchImg(object):
    def __init__(self,operating_system,widget_img_path,discern_img_path,assign_area=None,confidence=None):
        """
        :param operating_system:哪一端的图片（android or ios）
        :param widget_img_path:控件图
        :param discern_img_path:待识别图片（图片上是否有指定控件）的路径
        :param assign_area:为了提高识别率，可以指定将待识别图片裁剪的一个区域
        :param confidence:指定识别的置信率，默认为0.7
        """
        # self.LOG_STATUS = get_yaml_config_info(yaml_path=os.path.join(current_path, 'config.yml').replace('\\', '/'))[
        #     'LOG_LEVEL']
        self.operating_system=operating_system
        self.window_y,self.window_x=self.get_image_resolve(discern_img_path=discern_img_path)
        self.widget_img_path=widget_img_path
        # Logger(LOG_STATUS=self.LOG_STATUS).setlog('self.widget_img_path:  ' + str(self.widget_img_path))
        # Logger(LOG_STATUS=self.LOG_STATUS).setlog('self.window_x:  ' + str(self.window_x))
        # Logger(LOG_STATUS=self.LOG_STATUS).setlog('self.window_y:  ' + str(self.window_y))
        self.discern_img_path=discern_img_path
        # Logger(LOG_STATUS=self.LOG_STATUS).setlog('self.discern_img_path:  ' + str(self.discern_img_path))
        self.confidence=confidence if confidence else 0.7
        # Logger(LOG_STATUS=self.LOG_STATUS).setlog('self.confidence:  ' + str(self.confidence))
        self.assign_area = assign_area if assign_area else [0.0, 0.0, 1.0, 1.0]
        # Logger(LOG_STATUS=self.LOG_STATUS).setlog('self.assign_area:  ' + str(self.assign_area))



    def screenshot_element_by_resize(self,img_file, element=''):
        """
        在全屏图基础上截取指定区域，返回坐标信息
        :param img_file: 图片保存位置
        :param element: (location_x,location_y,width,height)表示（截图区域左上角的坐标(x,y)，以及截图的宽度和高度）
        :return: True, location_x, location_y, size_width, size_height, scale_x, scale_y
        """
        percent_location_x, percent_location_y, percent_width, percent_height = element

        # 手机屏幕上显示的截图位置
        location_x, location_y = int(self.window_x * percent_location_x), int(
            self.window_y * percent_location_y)
        # 手机上截图的宽和高
        size_width, size_height = int(self.window_x * percent_width), int(self.window_y * percent_height)

        screenshot_origin = self.read_img(img_file)
        # 截图在PC上的尺寸
        screenshot_origin_width, screenshot_origin_height = screenshot_origin.shape[1], screenshot_origin.shape[0]

        # 要截取的实际位置和宽高（PC上显示的位置）
        pc_location_x, pc_location_y, pc_width, pc_height = int(percent_location_x * screenshot_origin_width), int(
            percent_location_y * screenshot_origin_height), int(percent_width * screenshot_origin_width), int(
            percent_height * screenshot_origin_height)
        # 重新截取指定区域位置的图片覆盖原图
        # 按照坐标截图保存覆盖截图
        fp = open(img_file, 'rb')
        im = Image.open(fp)

        im.crop((pc_location_x, pc_location_y, pc_location_x + pc_width, pc_location_y + pc_height)).save(img_file)

        scale_x, scale_y = percent_width, percent_height
        fp.close()
        return True, location_x, location_y, size_width, size_height, scale_x, scale_y

    def screen_and_get_position(self,img_file):
        """
        截图，整个屏幕 / 指定控件所在区域
        :param img_file:存储的截图文件路径及名字，例如../temp.png
        :return:截图的位置的信息，position={'location_x':'xxx','location_y':'yyy','size_width':'xxx','size_height':'yyy'}
                location_x,location_y为截图左上角在屏幕中的位置，全屏的location为(0,0)。size为截图的宽高尺寸
        """
        # (location_x,location_y,width,height)表示（截图区域左上角的坐标(x,y)，以及截图的宽度和高度）
        location_x, location_y, size_width, size_height, scale_x, scale_y = self.screenshot_element_by_resize(img_file, element=self.assign_area)[1:]

        position = {'location_x': location_x, 'location_y': location_y, 'size_width': size_width,
                    'size_height': size_height}
        self.scale_x, self.scale_y = scale_x, scale_y  # 存储截图在原图中的占比，用来计算PC中的实际尺寸
        return position

    # 查找文件名称中包含filename的图片
    def find_img_by_name(self,search_path, filename):
        """

        :param search_path: 框架中存放图片的目录
        :param filename: 待识别图片的文件名
        :return:文件名，将与待识别图片比对的框架中存放图片的路径
        """
        if '\\' in filename:
            filename = filename.replace("\\", "/")
        index = len(filename)
        for p in os.listdir(search_path):
            if os.path.isdir(os.path.join(search_path, p)):
                file_name, result = self.find_img_by_name(os.path.join(search_path, p), filename)
                if result is None:
                    continue
                else:
                    return file_name, result
            elif p[:index] != filename or '.png' not in p:
                continue
            else:
                saved_file_name = str(p.replace('.png', ''))
                saved_file_name1 = saved_file_name.split('_(')[0]
                pa = str(os.path.join(search_path, p))
                if '\\' in pa:
                    pa = pa.replace("\\", "/")
                if saved_file_name1 == filename:
                    return p, pa
                else:
                    return p, pa
        return None, None

    # 根据窗口分辨率查找 文件名称中有匹配分辨率的图片
    def find_img_by_pixel(self,search_path, filename):
        """

        :param search_path:框架中存放图片的目录
        :param filename:待识别图片的文件名
        :return:文件名，将与待识别图片比对的框架中存放图片的路径
        """
        for p in os.listdir(search_path):
            if os.path.isdir(os.path.join(search_path, p).replace('\\', '/')):  #是目录的话继续查找
                file_name, result = self.find_img_by_pixel(os.path.join(search_path, p).replace('\\', '/'), filename)
                if result is None:
                    continue
                else:
                    return file_name, result
            else:
                if PLATFORM_IOS in self.operating_system and int(self.window_x) > 400:
                    # iOS self.window_x self.window_y 返回的值是pt 值， 不是px分辨率的值，需要再计算
                    # px: 像素单位
                    # ppi: Pixels Per Inch 每英寸拥有的像素数目，屏幕像素密度 ，ppi = 根号（x 方 + y 方） / 屏幕尺寸
                    # pt：ios开发单位，point 即绝对长度 1 pt = 1 / 72 英寸
                    # Plus系列 截图分辨率都是 pt * 3 ， 实际屏幕分辨率是pt * 3 / 1.15
                    x = int(int(self.window_x) * 3 / 1.15)
                    y = int(int(self.window_y) * 3 / 1.15)
                elif PLATFORM_IOS in self.operating_system:
                    # 除 Plus 外其他机型分辨率都是 pt * 2
                    x = int(self.window_x) * 2
                    y = int(self.window_y) * 2
                else:
                    # android 手机 直接获取的就是
                    x = self.window_x
                    y = self.window_y
                if str(x) in p and str(y) in p and filename in p:  #保证基准图名称+分辨率是匹配的
                    path = os.path.join(search_path, p)
                    if '\\' in path:
                        path = path.replace('\\', '/')
                    print("p:",p)
                    print("path:",path)
                    print("str(x):",str(x))
                    print("str(y):",str(y))
                    return p, path
                else:
                    continue
        return None, None

    def find_assign_img(self, filename):
        """
        :param filename: 文件名
        :return:是否在框架中找到与待识别图片进行识别的图片，图片名称，图片对象
        """
        project_dir=pics_set_dir
        print("project_dir:",project_dir)
        print("filename:",filename)
        img_obj_name, img_obj = self.find_img_by_pixel(project_dir, filename)
        print('根据分辨率查找img_obj_name: ',img_obj_name)
        print('根据分辨率查找img_obj:  ',img_obj)
        if img_obj is None:
            img_obj_name, img_obj = self.find_img_by_name(project_dir, filename)
            print('根据名称查找img_obj_name：  ',img_obj_name)
            print('根据名称查找img_obj：   ',img_obj)
            if img_obj is None:
                print("没有在基准图目录下找到图片")
                return False, None, None
        return True, img_obj_name, img_obj

    def match_img(self,screen, image):
        """
        :param screen:判断的屏幕截图
        :param image:查找到控件定位图
        :return:返回匹配结果
        """
        # Logger(LOG_STATUS=self.LOG_STATUS).setlog('screen:  '+str(screen))
        # Logger(LOG_STATUS=self.LOG_STATUS).setlog('image:  ' + str(image))
        img = Template( filename=image,threshold=self.confidence)
        screen_image = self.read_img(screen)
        match_result = img._cv_match(screen_image)
        if match_result is not None:
            match_result['shape'] = (screen_image.shape[1], screen_image.shape[0])  # 0为高，1为宽
        return match_result

    # 相似度大于confidence时，返回中心坐标点，否则返回False
    def get_point(self,screen,  image):
        """

        :param screen:原图源
        :param image:截图源
        :return:识别出来的坐标
        """
        match_result = self.match_img(screen,  image)  # 识别算法
        if match_result is None:
            return False, None, None

        confidence_result = match_result["confidence"]
        position = tuple(map(int, match_result['result']))

        recognition_area = match_result['rectangle']
        l1, l2 = recognition_area[0]
        r1, r2 = recognition_area[2]
        im = Image.open(screen)
        outdraw = ImageDraw.Draw(im)
        outdraw.rectangle((l1, l2, r1, r2), outline="red")
        im.save(screen)
        if confidence_result > self.confidence:

            position_info = {'position': position, 'shape': match_result['shape']}
            print('position_info', position_info)
            return True, position_info, confidence_result
        else:
            return False, None, None

    def return_coor_by_img(self):
        """
        返回控件在图片中的坐标
        :return: 如果成功查找到控件则返回实际坐标元组 x,y，否则为None ,None
        """
        position_x = None
        position_y = None
        img_is_existed, img_obj_name, img_obj = self.find_assign_img(filename=self.widget_img_path.split('/')[-1])

        #img_obj=self.widget_img_path

        discern_img_can_recogn=False
        # 获取截图的坐标和尺寸（手机上显示的）
        photo_position = self.screen_and_get_position(self.discern_img_path)
        # 截图在手机上显示的位置的宽高尺寸
        photo_position_x = int(photo_position['location_x'])
        photo_position_y = int(photo_position['location_y'])
        photo_width = int(photo_position['size_width'])
        photo_height = int(photo_position['size_height'])
        print("self.discern_img_path:",self.discern_img_path)
        print("img_obj:",img_obj)
        status, position, rec_confidence = self.get_point(screen=self.discern_img_path, image=img_obj)
        print("status:",status)
        print("position:", position)
        print("rec_confidence:",rec_confidence)
        if status:
            x, y = position['position']
            shape = (position['shape'])
            shape_x = int(shape[0])
            shape_y = int(shape[1])
            position_x = int(photo_position_x + (photo_width / shape_x * x))
            position_y = int(photo_position_y + (photo_height / shape_y * y))
        print("rec_confidence:",rec_confidence)
        print("self.confidence:",self.confidence)
        if rec_confidence is None:
            return discern_img_can_recogn, rec_confidence,[position_x, position_y]
        if rec_confidence>self.confidence:
            discern_img_can_recogn=True
        # Logger(LOG_STATUS=self.LOG_STATUS).setlog('rec_confidence:  '+str(rec_confidence))
        return discern_img_can_recogn, rec_confidence,[position_x, position_y]


    # 得到图片分辨率
    def get_image_resolve(self,discern_img_path=''):
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
    def read_img(self,src):
        """
        :param src:图片的路径
        :return:返回图片数据
        """
        return cv2.imdecode(np.fromfile(src, dtype=np.uint8), 100)




