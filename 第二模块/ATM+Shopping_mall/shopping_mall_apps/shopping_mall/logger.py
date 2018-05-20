#-*- coding:utf-8 -*-
import os,sys
import logging
from conf import settings
from logging import handlers
def logger(log_type):
    logger_obj=logging.getLogger(log_type)
    logger_obj.setLevel(settings.LOG_LEVEL)
    #log_file=os.path.join(settings.LOG_PATH,"%s.log" % log_type)
    log_file=os.path.join(settings.LOG_PATH,settings.LOG_TYPES[log_type])
    file_handler=logging.FileHandler(log_file)
    #file_handler=logging.handlers.RotatingFileHandler(log_file,maxBytes=10, backupCount=3)
    logger_obj.addHandler(file_handler)
    file_formatter=settings.LOG_FORMAT
    file_handler.setFormatter(file_formatter)
    return logger_obj