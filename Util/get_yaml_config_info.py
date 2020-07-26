# *_*coding:utf-8 *_*
import os

import yaml


def get_yaml_config_info(yaml_path):
    """
    :param yaml_path:yaml文件的路径
    :return:yaml 字典
    """
    f = open(yaml_path, encoding='utf-8')
    yaml_dict = yaml.load(f, Loader=yaml.FullLoader)
    f.close()
    return yaml_dict


