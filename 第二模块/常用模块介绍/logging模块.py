import logging
from logging import handlers
#日志级别由低到高 debug info warnning,errror,critical
#logging.warning("hello,woranning")
#logging.critical("server is down")

# logging.basicConfig(filename="log_test.log",level=logging.INFO,
#                     format="%(asctime)s %(filename)s:%(funcName)s:%(lineno)d:%(process)s %(message)s",
#                     datefmt="%Y-%m-%d %H:%M:%S %p")  #level 是输出日志级别比INFO和比他高级别的日志
# def sayhi():
#     logging.error("print line number")
# sayhi()
# logging.debug("this message should go to log file")
# logging.warning("hello,woranning")
# logging.critical("server is down")


###logging 模块进阶
#1 生成logger对象
#2.生成handler对象  --有文件handler，console的handler，等
#2.1 把handler对象绑定到logger对象
#3.生成formatter对象
#3.1 把format对象绑定到handler对象

#option：  filter学习
class  ScottIgnoredbbackupFilter(logging.Filter):
    def filter(self,record):
        return 'db backup' not in record.getMessage()   #得到函数返回值，True 或者 False


#举一个案例，让日志同时输出到文件和屏幕
logger=logging.getLogger("scott_website") #logger对象生成
logger.setLevel(logging.DEBUG)   #演示日志级别效果
console_handler=logging.StreamHandler() #console handler生成
file_handler=logging.FileHandler("scott_website.log")   #文件handler生成
#console_handler.setLevel(logging.WARNING)   #handler也可以设置日志级别

logger.addHandler(console_handler)   #绑定handler 到logger
logger.addHandler(file_handler)

#formatter对象生成
console_formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s -%(lineno)d - %(message)s')
file_formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

console_handler.setFormatter(console_formatter)   #绑定到handler
file_handler.setFormatter(file_formatter)

#可选的，一般filter不咋用。  是 True就记录日志，False不记录
logger.addFilter(ScottIgnoredbbackupFilter())

#执行
logger.warning("test warnning log ")
logger.info("test info log")
logger.debug("test debug log db backup")

#logger应该设置一个日志级别。没有的话 默认logger全局配置日志级别为warnning. 同时handler也可以设置日志级别，
#其实他们共同起作用，当Global级别比handler高时，以全局级别为准，反之则以handler为准。也就是以谁高按谁来。






