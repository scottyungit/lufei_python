#-*- coding:utf-8 -*-
from shopping_mall.load_card import authenticate_credit_card

def login(func):
    def wrapper(user_obj,atm_user_obj,good_obj,access_logger,transaction_logger):
        # global user_obj
        # print(user_obj)
        # global access_logger
        if atm_user_obj["is authenticated"] == True:
            func(user_obj,atm_user_obj,good_obj,access_logger,transaction_logger)
        else:
            print("您的帐户还没有认证,请先进行认证")
            retry = 0
            while atm_user_obj["is authenticated"] is not True:
                account = input("\033[1;31;40m" + "please enter your username: " + "\033[0m").strip()
                password = input("\033[1;31;40m" + "please enter your password: " + "\033[0m").strip()
                auth_data = authenticate_credit_card(account, password)
                if auth_data:  # 已经拿到账户数据
                    atm_user_obj["is authenticated"] = True
                    atm_user_obj['data'] = auth_data
                    print("\033[42;1m信用卡验证成功\033[0m")
                    # 记录日志
                    access_logger.info("user %s logged in" % atm_user_obj['data']['id'])
                    # 开始具体功能
                    func(user_obj, atm_user_obj, good_obj, access_logger, transaction_logger)
                else:
                    print("wrong account or password.Authenticating Failed!")
                if retry == 3:
                    error_message = "你已经尝试了3次错误的用户名密码,无法继续！"
                    print(error_message)
                    exit()
    return wrapper