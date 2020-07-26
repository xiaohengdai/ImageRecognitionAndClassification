# encoding:utf-8

"""
工具说明：打印log
使用方法：引入log.py文件，打印日志方法Logger().log(VALUE,LEVEL)
"""
import datetime
import logging
import logging.handlers
import os
import sys
import traceback

from colorama import Fore, Style

current_path = os.path.abspath(os.path.dirname(__file__))
print('log中current_path :   ',current_path )
pro_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".").replace('\\', '/')
LEVEL_ERROR = 'ERROR'
LEVEL_EXCEPTION = "EXCEPTION"
LEVEL_CRITICAL = "CRITICAL"
LEVEL_INFO = "INFO"
LEVEL_DEBUG = "DEBUG"

LEVEL_INDEX = {
    LEVEL_DEBUG: 0,
    LEVEL_INFO: 1,
    LEVEL_ERROR: 2,
    LEVEL_EXCEPTION: 3,
    LEVEL_CRITICAL: 4,
}


class Logger(object):
    def __init__(self, model_name='',LOG_STATUS="INFO"):
        self.LEVEL_ERROR = 'ERROR'
        self.LEVEL_EXCEPTION = "EXCEPTION"
        self.LEVEL_CRITICAL = "CRITICAL"
        self.LEVEL_INFO = "INFO"
        self.LEVEL_DEBUG = "DEBUG"
        self.full_log_file = pro_path + '/' + 'run_log.txt'
        #print('self.full_log_file:  ',self.full_log_file)
        self.model_name = model_name
        self.LOG_STATUS=LOG_STATUS
        self.init_full_log_file()



    """
        log():只是保存log到本地log.txt以及输出到控制台
        setlog():保存log到本地log.txt以及输出到控制台，同时追加log到测试结果中，最终显示在报告内
        :param VALUE: 具体要存储的log内容，只能是str或异常e
        :param LEVEL: log等级，默认为info
        :return: 无
    """

    def init_full_log_file(self):
        if os.path.exists(self.full_log_file):
            os.remove(self.full_log_file)
            #print('清除之前的文件成功')
        #     self.LOG_STATUS = True
        #
        # if not os.path.exists(self.full_log_file):
        #     with open(self.full_log_file, 'w') as file:
        #         file.close()
        #         pass

    def log(self, value="", log_level=LEVEL_INFO, func_name='', line_number=0):
        fmt = logging.Formatter(fmt="[%(asctime)s] <%(name)s>  %(message)s", datefmt='%m.%d %H:%M:%S')
        # console_handler = logging.StreamHandler()  # 将日志同时输出到屏幕和日志文件
        # console_handler.setFormatter(fmt)
        if len(self.model_name) != 0:
            func_name = self.model_name
        elif len(func_name) == 0:
            func_name = sys._getframe().f_back.f_code.co_filename.split(os.path.sep)[-1][:-3]  # 获取调用文件名
        if line_number == 0:
            line_number = sys._getframe().f_back.f_lineno  # 获取行号
        _log = logging.getLogger(func_name + ':' + str(line_number))  # 返回1个log对象
        # _log.addHandler(console_handler)  # 把日志添加进去

        file_handler = None

        # ---------------------------------------- 设备log ------------------------------------------
        # device_log_file 是要输出的单个设备的日志文件地址


        # ----------------------------------------- 汇总log ------------------------------------------
        # log 汇总文件

        if not os.path.exists(self.full_log_file):
            with open(self.full_log_file, 'w') as file:
                file.close()
                pass
        full_handler = logging.FileHandler(self.full_log_file, encoding="utf-8")
        full_handler.setFormatter(fmt)
        _log.addHandler(full_handler)

        _log.setLevel(self.LOG_STATUS)
        if LEVEL_INDEX[log_level] >= LEVEL_INDEX[self.LOG_STATUS]:
            if log_level == LEVEL_EXCEPTION:
                self.print_error(value, func_name, str(line_number))
            elif log_level == LEVEL_CRITICAL:
                self.print_error(value, func_name, str(line_number))
            elif log_level == LEVEL_DEBUG:
                self.print_debug(value, func_name, str(line_number))
            elif log_level == LEVEL_ERROR:
                self.print_error(value, func_name, str(line_number))
            elif log_level == LEVEL_INFO:
                self.print_log(value, func_name, str(line_number))
            else:
                print('此log的等级不存在')
                assert False

        if log_level == LEVEL_EXCEPTION:
            _log.exception(Fore.RED + value + Style.RESET_ALL)
        elif log_level == LEVEL_CRITICAL:
            _log.critical(Fore.GREEN + value + Style.RESET_ALL)
        elif log_level == LEVEL_DEBUG:
            _log.debug(Fore.WHITE + value + Style.RESET_ALL)
        elif log_level == LEVEL_ERROR:
            _log.error(Fore.BLUE + value + Style.RESET_ALL)
        elif log_level == LEVEL_INFO:
            _log.info(Fore.CYAN + value + Style.RESET_ALL)
        else:
            print('此log的等级不存在')
            assert False
        # self.print_log(value, func_name, str(line_number))
        # _log.removeHandler(console_handler)
        try:
            #print('file_handler:    ',file_handler)
            if file_handler is not None:
                file_handler.close()
            if full_handler is not None:
                full_handler.close()
            _log.removeHandler(file_handler)
            _log.removeHandler(full_handler)
        except Exception as e:
            print(traceback.format_exc())
            pass

    def setlog(self, value, level=LEVEL_INFO, func_name='', line_number=0):
        """
        保存log到本地log.txt，同时追加log到测试结果中，最终显示在报告内
        :param value: 具体要存储的log内容，只能是str或异常e
        :param level: log等级，默认为info
        :param func_name: Log中显示的函数名
        :param line_number: Log所在行号
        :return: 无
        """
        time = datetime.datetime.now().strftime("%m.%d %H:%M:%S")
        frame = sys._getframe()
        if len(self.model_name) != 0:
            func_name = self.model_name
        elif len(func_name) == 0:
            # 获取调用文件名
            func_name = frame.f_back.f_code.co_filename.split(os.path.sep)[-1][:-3] + '.' + frame.f_back.f_code.co_name
        if line_number == 0:
            # 获取行号
            line_number = frame.f_back.f_lineno

        self.log(value, level, func_name, line_number)
        # 只有通过runtest中的@test运行的脚本才会初始化resultinfos["log"]的值，否则不追加日志


    @staticmethod
    def print_log(message, frame='JAR.VIS', line_no=None):
        """
        控制台 框架 log 彩色 输出, 【时间】<函数：行号> 内容
        :param line_no: 行号
        :param frame: 显示的模块名
        :param message: 打印内容
        :return: 无
        """
        try:
            level = Fore.BLUE + '[I]' + Fore.RESET
            time_now = Fore.MAGENTA + '[' + str(datetime.datetime.now().strftime("%m.%d %H:%M:%S.%f"))[
                                            :-3] + ']' + Fore.RESET
            if line_no:
                frame = Fore.CYAN + '<' + frame + ":" + Fore.RESET + Fore.WHITE + line_no + Fore.RESET + Fore.CYAN + ">" + Fore.RESET
            else:
                frame = Fore.CYAN + '<' + frame + ">" + Fore.RESET
            print(level, time_now, frame, ' ' + Fore.YELLOW + str(message) + Fore.RESET)
        except:
            import traceback
            try:
                print('Log打印异常', traceback.format_exc())
            except:
                pass

    @staticmethod
    def print_debug(message, frame='JAR.VIS', line_no=None):
        """
        控制台 框架 log 彩色 输出, 【时间】<函数：行号> 内容
        :param line_no: 行号
        :param frame: 显示的模块名
        :param message: 打印内容
        :return: 无
        """
        try:
            level = '[D]'
            time_now = '[' + str(datetime.datetime.now().strftime("%m.%d %H:%M:%S.%f"))[:-3] + ']'
            if line_no:
                frame = '<' + frame + ":" + line_no + ">"
            else:
                frame = '<' + frame + ">"
            print(Fore.WHITE + level + ' ' + time_now + ' ' + frame + '  ' + str(message) + Fore.RESET)
        except:
            import traceback
            try:
                print('Log打印异常', traceback.format_exc())
            except:
                pass

    @staticmethod
    def print_error(message, frame='JAR.VIS', line_no=None):
        """
        控制台 框架 log 彩色 输出, 【时间】<函数：行号> 内容
        :param line_no: 行号
        :param frame: 显示的模块名
        :param message: 打印内容
        :return: 无
        """
        try:
            level = '[E]'
            time_now = '[' + str(datetime.datetime.now().strftime("%m.%d %H:%M:%S.%f"))[:-3] + ']'
            if line_no:
                frame = '<' + frame + ":" + line_no + ">"
            else:
                frame = '<' + frame + ">"
            print(Fore.RED + level + ' ' + time_now + ' ' + frame + '  ' + str(message) + Fore.RESET)
        except:
            import traceback
            try:
                print('Log打印异常', traceback.format_exc())
            except:
                pass
