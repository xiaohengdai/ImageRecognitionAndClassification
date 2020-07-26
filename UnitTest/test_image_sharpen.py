# *_*coding:utf-8 *_*
import os
import unittest


from ImagePretreatment.image_sharpen import image_sharpen

current_path = os.path.abspath(os.path.dirname(__file__))
current_path = current_path.replace("\\", "/")

class TestImageSharpen(unittest.TestCase):
    def test_image_sharpen(self):
        img_src = current_path + "/ImgReco/small_tool_1.png"
        img_dst = img_src.split('.')[0] + '_temp1.png'
        image_sharpen(img_src, img_dst)

if __name__ == '__main__':
    unittest.main()