from .logger import logger
from .auth import   authenticate
from atm import logics
#from atm.logics import view_account_info,with_draw,pay_back,transfer
#from atm.utils import print_error
#from .db_handler import

access_logger=logger("access")
transaction_logger=logger("transaction")
#admin_logger=logger("admin")
##user对象
user_obj={
    "is authenticated": False,
    "data":None,
}
#功能
features=[
    ("查看账户信息",logics.view_account_info),
    ("取钱",logics.with_draw),
    ("还钱",logics.pay_back),
    ("转账",logics.transfer),
]

def controller(user_obj):
    while True:
        for index,feature in enumerate(features):
            print(index,": ",feature[0])
        choice=input("\033[1;31;40m"+">>>输入编号选择功能(输入'q'可以退出): "+"\033[0m").strip()
        if not choice:continue
        if choice.isdigit():
            if int(choice)<len(features):
                choice=int(choice)
                features[choice][1](user_obj,access_logger=access_logger,transaction_logger=transaction_logger)

            else:
                print("值必须小于"+len(features)+"请重新输入！")
                continue
        if choice=="q":exit("Goodbye")

def entrance():
    retry = 0
    while user_obj["is authenticated"] is not True:
        account=input("\033[1;31;40m"+"please enter your account: "+"\033[0m").strip()
        password=input("\033[1;31;40m"+"please enter your password: "+"\033[0m").strip()
        auth_data=authenticate(account,password)
        if auth_data:   #已经拿到账户数据
            user_obj["is authenticated"]=True
            user_obj['data']=auth_data
            print("welcome %s" % user_obj['data']['id'])
            #记录日志
            access_logger.info("user %s logged in" % user_obj['data']['id'])
            #开始具体功能
            controller(user_obj)
        else:
            print("wrong usename 或者 password")
            retry += 1
        if retry == 3:
            error_message="你已经尝试了3次错误的用户名密码！"
            print(error_message)
            #记录日志
            break

