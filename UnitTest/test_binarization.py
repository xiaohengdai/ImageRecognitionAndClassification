# *_*coding:utf-8 *_*
import unittest
import os
import sys
sys.path.append("/Users/xiaoheng/Downloads/meituan/ImageRecognitionAndClassification")
from ImagePretreatment.binarization import binary_local_threshold

current_path = os.path.abspath(os.path.dirname(__file__))
current_path = current_path.replace("\\", "/")

class TestBinarization(unittest.TestCase):
    def test_binarization(self):
        #img_src = current_path+"/ImgReco/small_tool_2.png"
        img_src ="/Users/xiaoheng/Downloads/meituan/ocr/ocr_img/我常买弹窗.jpeg"
        img_dst = img_src.split('.')[0] + '_binarization.png'
        binary_local_threshold(img_src, img_dst)


if __name__=='__main__':
    unittest.main()