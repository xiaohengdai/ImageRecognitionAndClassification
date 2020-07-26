# *_*coding:utf-8 *_*
import os
import shutil
import unittest
import sys
sys.path.append("/Users/xiaoheng/Downloads/meituan/ImageRecognitionAndClassification")
from ImagePretreatment.gray_scale import gray_scale
import os

current_path = os.path.abspath(os.path.dirname(__file__))
current_path = current_path.replace("\\", "/")

class TestGrayScale(unittest.TestCase):
    def test_gray_scale(self):
        #img_src_path = current_path+'/ImgReco/small_tool.png'
        img_src_path="/Users/xiaoheng/Downloads/meituan/ocr/ocr_img/我常买弹窗.jpeg"
        # img_src_path = current_path + '/ImgReco/small_tool.png'
        img_dst_path = img_src_path.split('.')[0] + '_gray_scale.png'
        print('img_dst_path:    ',img_dst_path)
        #shutil.copy(img_src_path, img_dst_path)
        gray_scale(img_src_path, img_dst_path)


if __name__ == '__main__':
    unittest.main()