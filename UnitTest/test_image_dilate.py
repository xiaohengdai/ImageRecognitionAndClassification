# *_*coding:utf-8 *_*
import unittest
import os
import sys
sys.path.append("/Users/xiaoheng/Downloads/meituan/ImageRecognitionAndClassification")
from ImagePretreatment.image_dilate import image_dilate

current_path = os.path.abspath(os.path.dirname(__file__))
current_path = current_path.replace("\\", "/")


class TestImageDilate(unittest.TestCase):

    def test_image_dilate(self):
        #print("current_path:", current_path)
        img_src = "/Users/xiaoheng/Downloads/meituan/ocr/ocr_img/我常买弹窗.jpeg"
        #img_src=current_path+"/ImgReco/small_tool_1.png"
        img_dst = img_src.split('.')[0] + '_image_dilate.png'
        image_dilate(img_src,img_dst)

if __name__ == '__main__':
    unittest.main()