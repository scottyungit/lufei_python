#-*- coding:utf-8 -*-
import os,json
from conf import settings
from .logger import logger
from .auth import   authenticate
from shopping_mall import logics
from shopping_mall import load_card

access_atm_logger=logger("access from shopping_mall")
transaction_logger=logger("transaction")
#admin_logger=logger("admin")
atm_user_obj={
    "is authenticated": False,
    "data":None,
}
##user对象
user_obj={
    "is authenticated": False,
    "data":None,
}

#功能
features=[
    ("查看购买历史纪录",logics.view_shopping_info),
    ("购买",logics.add_shopping_cart),
]
good_file = settings.DB_GOODS_FILE
if os.path.isfile(good_file):  # 判断一个PATH是不是一个文件。是就为True
    f = open(good_file,encoding="utf-8")
    good_obj = json.load(f)
    f.close()
else:
    print("The goods file is not exists")

def controller(user_obj):
    while True:
        for index,feature in enumerate(features):
            print(index,": ",feature[0])
        choice=input(">>>输入编号选择功能(输入'q'可以退出): ").strip()
        if not choice:continue
        if choice.isdigit():
            if int(choice)<len(features):
                choice=int(choice)
                features[choice][1](user_obj,atm_user_obj,good_obj,access_logger=access_atm_logger,transaction_logger=transaction_logger)

            else:
                print("值必须小于"+len(features)+"请重新输入！")
                continue
        if choice=="q":exit("Goodbye")

def entrance():
    retry = 0
    while user_obj["is authenticated"] is not True:
        account=input("please enter your accounts: ").strip()
        password=input("please enter your password: ").strip()
        auth_data=authenticate(account,password)
        if auth_data:   #已经拿到账户数据
            user_obj["is authenticated"]=True
            user_obj['data']=auth_data
            print("\033[42;1mWelcome %s\033[0m" % user_obj['data']['username'])
            #credit card 验证
            print("-------请验证您的信用卡帐户-------")
            load_card.load_atm_user_obj_data(atm_user_obj,access_atm_logger)
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


