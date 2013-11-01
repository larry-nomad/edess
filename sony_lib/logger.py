# -*- coding: utf-8 -*-
"""

auth:   jaypei
email:  jaypei97159@gmail.com

例程：
from somelib import logger

# 默认log存放目录,需要在程序入口调用才能生效,可省略
logger.log_dir = "./app"
# log文件名前缀,需要在程序入口调用才能生效,可省略
logger.log_name = "test_log"

conf = logger.Logger()
conf.debug('debug')
conf.info('ds-info')
conf.error('ss-error')

"""

import logging
import logging.handlers
import os
import threading
import time

try:
    import codecs
except ImportError:
    codecs = None

log_dir = "log"
log_name = "applog"

_logger_init_lock = threading.Lock()


class MyHandler(logging.handlers.TimedRotatingFileHandler):
    """
    自己定义的TimedRotatingFileHandler
    """
    def __init__(self, log_dir, file_name_prefix):
        self.log_dir = log_dir
        self.file_name_prefix = file_name_prefix

        self._mkdirs()

        self.baseFilename = "%s.%s.log" % (os.path.join(self.log_dir, file_name_prefix), time.strftime("%Y%m%d"))

        logging.handlers.TimedRotatingFileHandler.__init__(self,
                                                           self.baseFilename,
                                                           when='midnight', interval=1,
                                                           backupCount=0, encoding=None)

    def doRollover(self):
        self.stream.close()
        # get the time that this sequence started at and make it a TimeTuple
        self.baseFilename = "%s.%s.log" % (os.path.join(self.log_dir, self.file_name_prefix),
                                           time.strftime("%Y%m%d"))
        if self.encoding:
            self.stream = codecs.open(self.baseFilename, 'a', self.encoding)
        else:
            self.stream = open(self.baseFilename, 'a')
        self.rolloverAt = self.rolloverAt + self.interval

    def _mkdirs(self):
        if not os.path.exists(self.log_dir):
            try:
                os.makedirs(self.log_dir)
            except Exception, e:
                print str(e)


class Logger(object):
    __instance = None

    def __new__(classtype, *args, **kwargs):
        _logger_init_lock.acquire()
        if classtype != type(classtype.__instance):
            classtype.__instance = object.__new__(classtype, *args, **kwargs)
            classtype.__instance.init()

        _logger_init_lock.release()
        return classtype.__instance

    def init(self):
        # 创建日志目录
        global log_dir, log_name
        self.log_dir = log_dir
        self.log_name = log_name

        self.is_debug = True
        self.is_info = True
        self.is_error = True

        self.logger_formatter = "[%(asctime)-15s,%(levelname)s] %(message)s"
        self.file_formatter = "[%(asctime)-15s,%(levelname)s] %(message)s"
        self._initLogger()

    def _initLogger(self):
        # 初始化logger
        logging.basicConfig(format=self.logger_formatter)
        self._default_logger = logging.getLogger()
        self._info_logger = logging.getLogger("_sys_info")
        self._error_logger = logging.getLogger("_sys_error")
        self._debug_logger = logging.getLogger("_sys_debug")
        #self._default_logger.setLevel(logging.INFO)
        self._default_logger.setLevel(logging.ERROR)
        #self._default_logger.setLevel(logging.DEBUG)
        self._info_logger.setLevel(logging.INFO)
        self._error_logger.setLevel(logging.ERROR)
        self._debug_logger.setLevel(logging.DEBUG)

        # 文件隔离
        for t in (("default", logging.DEBUG, self._default_logger),
                  ("debug", logging.DEBUG, self._debug_logger),
                  ("info", logging.INFO, self._info_logger),
                  ("error", logging.ERROR, self._error_logger)):

            filehandler = MyHandler(self.log_dir, "%s.%s" % (self.log_name, t[0]))
            filehandler.suffix = "%Y%m%d.log"
            filehandler.setLevel(t[1])
            filehandler.setFormatter(logging.Formatter(self.file_formatter))
            t[2].addHandler(filehandler)

    def enableDebug(self):
        self.is_debug = True

    def enableInfo(self):
        self.is_info = True

    def enableError(self):
        self.is_error = True

    def disableDebug(self):
        self.is_debug = False

    def disableInfo(self):
        self.is_info = False

    def disableError(self):
        self.is_error = False

    def debug(self, *args):
        if self.is_debug:
            self._debug_logger.debug(*args)

    def info(self, *args):
        if self.is_info:
            self._info_logger.info(*args)

    def error(self, *args):
        if self.is_error:
            self._error_logger.error(*args)


def info(*args):
    Logger().info(*args)


def debug(*args):
    Logger().debug(*args)


def error(*args):
    Logger().error(*args)
