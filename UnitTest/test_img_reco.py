import os
import shutil
import unittest
import sys
import time

sys.path.append("/Users/xiaoheng/Downloads/meituan/ImageRecognitionAndClassification")

from ImageRecognition.match_img import MatchImg

current_path = os.path.abspath(os.path.dirname(__file__))
current_path = current_path.replace("\\", "/")
parent_current_path=os.path.join(os.path.abspath(current_path+ "/" + ".."))

class TestImgReco(unittest.TestCase):
    def test_full_screen_area_img_reco1(self):
        print("执行的第一条TestCase")
        discern_img_path0='small_tool'
        discern_img_path=os.path.join(current_path,'ImgReco',discern_img_path0).replace("\\", "/")  #
        result_dir = discern_img_path.split('.')[0] + '_temp.png'
        img_src=discern_img_path+'.png'
        shutil.copy(img_src, result_dir)
        widget_img_path0='small_tool_(1440,2880).png'
        widget_img_path=parent_current_path+'/ImageRecognition/ReferenceImage/'+widget_img_path0
        print("result_dir:",result_dir)
        discern_img_can_recogn, rec_confidence, [position_x, position_y] = MatchImg(operating_system='android',widget_img_path=widget_img_path,discern_img_path=result_dir,assign_area=[0.85, 0.4, 0.15, 0.3]).return_coor_by_img()
        print('discern_img_can_recogn:  ',discern_img_can_recogn)
        print('rec_confidence:  ', rec_confidence)
        print('position_x:  ', position_x)
        print('position_y；  ', position_y)

    def test_full_screen_area_img_reco2(self):
        print("执行的第二条TestCase")
        start_time = time.time()
        #discern_img_path0 = 'camera_(843,1485)'
        #discern_img_path0 = 'camera_(720,1080)'
        discern_img_path0 = 'camera_(1080,1920)'
        discern_img_path = os.path.join(current_path, 'ImgReco', discern_img_path0).replace("\\", "/")  #
        result_dir = discern_img_path.split('.')[0] + '_temp.png'
        img_src = discern_img_path + '.png'
        shutil.copy(img_src, result_dir)
        #widget_img_path0 = 'camera_widget_big.png'
        widget_img_path0 = 'camera_widget_small.png'
        widget_img_path = parent_current_path + '/ImageRecognition/ReferenceImage/' + widget_img_path0
        print("result_dir:", result_dir)
        print(" widget_img_path:", widget_img_path)
        discern_img_can_recogn, rec_confidence, [position_x, position_y] = MatchImg(operating_system='android',
                                                                                    widget_img_path=widget_img_path,
                                                                                    discern_img_path=result_dir,
                                                                                    assign_area=[0.0, 0.0, 1.0,
                                                                                                 1.0]).return_coor_by_img()
        #此时从截图全屏中得到的识别率为0.538
        print('discern_img_can_recogn:  ', discern_img_can_recogn)
        print('rec_confidence:  ', rec_confidence)
        print('position_x:  ', position_x)
        print('position_y；  ', position_y)
        end_time = time.time()
        print("执行时间为:   ", str(end_time - start_time))


    def test_full_screen_area_img_reco3(self):
        print("执行的第三条TestCase，可以通过裁剪待处理图片的方式提高图片识别率")
        start_time=time.time()
        #discern_img_path0 = 'camera_(843,1485)'
        #discern_img_path0 = 'camera_(720,1080)'
        discern_img_path0 = 'camera_(1080,1920)'
        discern_img_path = os.path.join(current_path, 'ImgReco', discern_img_path0).replace("\\", "/")  #
        result_dir = discern_img_path.split('.')[0] + '_temp.png'
        img_src = discern_img_path + '.png'
        shutil.copy(img_src, result_dir)
        widget_img_path0 = 'camera_widget_big.png'
        widget_img_path = parent_current_path + '/ImageRecognition/ReferenceImage/' + widget_img_path0
        print("result_dir:", result_dir)
        # discern_img_can_recogn, rec_confidence, [position_x, position_y] = MatchImg(operating_system='android',
        #                                                                             widget_img_path=widget_img_path,
        #                                                                             discern_img_path=result_dir,
        #                                                                             assign_area=[0.7, 0.7, 0.3,
        #                                                                                          0.3]).return_coor_by_img()
        #
        # #此时从截图全屏中得到的识别率为0.55

        discern_img_can_recogn, rec_confidence, [position_x, position_y] = MatchImg(operating_system='android',
                                                                                    widget_img_path=widget_img_path,
                                                                                    discern_img_path=result_dir,
                                                                                    assign_area=[0.7, 0.8, 0.3,
                                                                                                 0.2]).return_coor_by_img()

        # 此时从截图全屏中得到的识别率为0.79,满足默认值0.7

        # 此时从截图全屏中得到的识别率为0.55
        end_time=time.time()
        print('discern_img_can_recogn:  ', discern_img_can_recogn)
        print('rec_confidence:  ', rec_confidence)
        print('position_x:  ', position_x)
        print('position_y；  ', position_y)
        print("执行时间为:   ",str(end_time-start_time))

    def test_full_screen_area_img_reco4(self):
        print("执行的第四条TestCase，可以通过调整基准图片的方式提高识别率")
        start_time = time.time()
        #discern_img_path0 = 'camera_(843,1485)'
        #discern_img_path0 = 'camera_(720,1080)'
        discern_img_path0 = 'camera_(1080,1920)'
        discern_img_path = os.path.join(current_path, 'ImgReco', discern_img_path0).replace("\\", "/")  #
        result_dir = discern_img_path.split('.')[0] + '_temp.png'
        img_src = discern_img_path + '.png'
        shutil.copy(img_src, result_dir)
        widget_img_path0 = 'camera_widget_small.png'
        widget_img_path = parent_current_path + '/ImageRecognition/ReferenceImage/' + widget_img_path0
        print("result_dir:", result_dir)
        # discern_img_can_recogn, rec_confidence, [position_x, position_y] = MatchImg(operating_system='android',
        #                                                                             widget_img_path=widget_img_path,
        #                                                                             discern_img_path=result_dir,
        #                                                                             assign_area=[0.0, 0.0, 1.0,
        #                                                                                          1.0]).return_coor_by_img()
        # # 此时从截图全屏中得到的识别率为0.44，采用上面的裁剪区域
        discern_img_can_recogn, rec_confidence, [position_x, position_y] = MatchImg(operating_system='android',
                                                                                    widget_img_path=widget_img_path,
                                                                                    discern_img_path=result_dir,
                                                                                    assign_area=[0.7, 0.8, 0.3,
                                                                                                 0.2]).return_coor_by_img()
        end_time = time.time()

        # # 此时从截图全屏中得到的识别率为0.81，采用上面的裁剪区域
        print('discern_img_can_recogn:  ', discern_img_can_recogn)
        print('rec_confidence:  ', rec_confidence)
        print('position_x:  ', position_x)
        print('position_y；  ', position_y)
        print("执行时间为:   ", str(end_time - start_time))



if __name__ == '__main__':
    # print(111)
    # unittest.main()
    # print(222)
    testunit=unittest.TestSuite()
    testunit.addTest(TestImgReco('test_full_screen_area_img_reco2'))
    #testunit.addTest(TestImgReco('test_full_screen_area_img_reco4'))
    unittest.TextTestRunner().run(testunit)