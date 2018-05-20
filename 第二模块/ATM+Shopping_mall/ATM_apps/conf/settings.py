#-*- coding:utf-8 -*-
import os,sys
import logging
#由于每个人安装软件的位置不确定，所以动态的找到我的根目录，以及DB文件的位置
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_ACCOUNTS_PATH=os.path.join(BASE_DIR,"db","accounts")
#全局定义了日志文件级别
LOG_LEVEL=logging.INFO
LOG_TYPES={"transaction":"transaction_log",
          "access":"access_log",
           "administration":"admin_log",
          }

LOG_FORMAT = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#LOG_PATH="%s/logs" % BASE_DIR,跟下面的效果一样，找到日志目录
LOG_PATH=os.path.join(BASE_DIR,"logs")
TRANSACTION_TYPE={
    "with_draw":{"action":"minus","interest":0.05},
    "pay_back":{"action":"plus","interest":0.0},
    "transfer":{"action":"transfer","interest":0.0}
}

ADMIN_FUNCTION={
}