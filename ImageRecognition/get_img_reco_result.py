# *_*coding:utf-8 *_*
import os
import shutil

from ImageRecognition.match_img import MatchImg


current_path=os.path.abspath(os.path.dirname(__file__)).replace('\\', '/')

def get_img_reco_result(src_img, dst_img, operating_system,confidence, type):
    """

    :param src_img: 待识别图片的路径
    :param confidence:识别的置信率
    :param type:0表示是否存在，1表示返回图片坐标
    :return:
    """

    #shutil.copy(dst_img,os.path.join(current_path,'ReferenceImage'))
    MatchImg(operating_system=operating_system,discern_img_path=src_img).return_coor_by_img()