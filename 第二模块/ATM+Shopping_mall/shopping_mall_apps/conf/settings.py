#-*- coding:utf-8 -*-
import os,sys
import logging
#由于每个人安装软件的位置不确定，所以动态的找到我的根目录，以及DB文件的位置
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_ACCOUNTS_PATH=os.path.join(BASE_DIR,"db","accounts")
DB_GOODS_FILE=os.path.join(BASE_DIR,"db","goods","goods.json")
ATM_BASE_DIR=os.path.join(os.path.dirname(BASE_DIR),"ATM_apps")
CREDIT_CARD_ACCOUNTS_PATH=os.path.join(ATM_BASE_DIR,"db","accounts")
#全局定义了日志文件级别
LOG_LEVEL=logging.INFO
LOG_TYPES={"access from shopping_mall":"access_log",
            "transaction":"transaction_log"}

LOG_FORMAT = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#LOG_PATH="%s/logs_bak" % BASE_DIR,跟下面的效果一样，找到日志目录
LOG_PATH=os.path.join(ATM_BASE_DIR,"logs")
