from atm.auth import authenticate

def login(func):
        def wrapper(user_obj,access_logger,transaction_logger):
            #global user_obj
            #print(user_obj)
            #global access_logger
            if user_obj["is authenticated"] == True:
                func(user_obj,access_logger,transaction_logger)
            else:
                print("您的帐户还没有认证,请先进行认证")
                retry = 0
                while user_obj["is authenticated"] is not True:
                    account = input("\033[1;31;40m" + "please enter your username: " + "\033[0m").strip()
                    password = input("\033[1;31;40m" + "please enter your password: " + "\033[0m").strip()
                    auth_data = authenticate(account, password)
                    if auth_data:  # 已经拿到账户数据
                        user_obj["is authenticated"] = True
                        user_obj['data'] = auth_data
                        print("welcome %s" % user_obj['data']['id'])
                        # 记录日志
                        access_logger.info("user %s logged in" % user_obj['data']['id'])
                        # 开始具体功能
                        func(user_obj,access_logger,transaction_logger)
                    else:
                        print("wrong usename 或者 password")
                        retry += 1
                    if retry == 3:
                        error_message = "你已经尝试了3次错误的用户名密码！"
                        print(error_message)
                        # 记录日志
                        break
        return wrapper