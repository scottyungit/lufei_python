import logging
from logging import handlers

###logging 模块进阶
#1 生成logger对象
#2.生成handler对象  --有文件handler，console的handler，等
#2.1 把handler对象绑定到logger对象
#3.生成formatter对象
#3.1 把format对象绑定到handler对象

#option：  filter学习
# class  ScottIgnoredbbackupFilter(logging.Filter):
#     def filter(self,record):
#         return 'db backup' not in record.getMessage()   #得到函数返回值，True 或者 False


#举一个案例，让日志同时输出到文件和屏幕
logger=logging.getLogger("scott_website") #logger对象生成
logger.setLevel(logging.DEBUG)   #演示日志级别效果
console_handler=logging.StreamHandler() #console handler生成
#file_handler=logging.FileHandler("scott_website_cut.log")   #文件handler生成
#console_handler.setLevel(logging.WARNING)   #handler也可以设置日志级别

#演示自动截断功能,maxBytes按照字节大小截断文件，backupCount保存几个日志备份
file_handler=logging.handlers.RotatingFileHandler("scott_website_cut.log",maxBytes=10, backupCount=3)

##演示按照时间自动截断功能,when和inerval控制时间，backupCount同上
file_handler=logging.handlers.TimedRotatingFileHandler("scott_website_time_cut_log",when="S",interval=1,backupCount=3)
logger.addHandler(console_handler)   #绑定handler 到logger
logger.addHandler(file_handler)

#formatter对象生成
console_formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(lineno)d [%(process)s]  %(message)s')
file_formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

console_handler.setFormatter(console_formatter)   #绑定到handler
file_handler.setFormatter(file_formatter)

#可选的，一般filter不咋用。  是 True就记录日志，False不记录
# logger.addFilter(ScottIgnoredbbackupFilter())

#执行
logger.warning("test warnning log ")
# logger.info("test info log")
# logger.debug("test debug log db backup")



##下面将日志的截断功能，属于handler的功能  效果就是 自动生成log.1 log.2 log.3
#按照字节去截断日志,重新命名新文件。加上.1 。如果.1存在，先将.1 替换为.2。再产生.1。就是说日志名字数字越大，就是越老的文件。
#logging.handlers.RotatingFileHandler
#按照时间去截断
#logging.handlers.TimedRotatingFileHandler