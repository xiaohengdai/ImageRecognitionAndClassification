# *_*coding:utf-8 *_*
import unittest
import os
import sys
sys.path.append("/Users/xiaoheng/Downloads/meituan/ImageRecognitionAndClassification")
current_path = os.path.abspath(os.path.dirname(__file__))
current_path = current_path.replace("\\", "/")

from ImagePretreatment.Image_blur import image_blur

class TestImageBlur(unittest.TestCase):
    def test_image_blur(self):
        #img_src=current_path+"/ImgReco/small_tool_1.png"
        img_src = "/Users/xiaoheng/Downloads/meituan/ocr/ocr_img/我常买弹窗.jpeg"
        img_dst = img_src.split('.')[0] + '_image_blur.png'
        image_blur(img_src,img_dst)

if __name__ == '__main__':
    unittest.main()
