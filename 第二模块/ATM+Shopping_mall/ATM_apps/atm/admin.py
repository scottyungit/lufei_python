from .logger import logger
from .auth import   authenticate
from atm import admin_logics

admin_logger=logger("administration")

user_obj={
    "is authenticated": False,
    "data":None,
}
#功能
features=[
    ("添加账户",admin_logics.add_account),
    ("添加额度",admin_logics.add_credit),
    ("冻结账户",admin_logics.froze_account),
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
                features[choice][1](user_obj,admin_logger=admin_logger,)

            else:
                print("值必须小于"+len(features)+"请重新输入！")
                continue
        if choice=="q":exit("Goodbye")


def entrance():
    retry = 0
    while user_obj["is authenticated"] is not True:
        account = input("\033[1;31;40m" + "please enter super username: " + "\033[0m").strip()
        password = input("\033[1;31;40m" + "please enter password: " + "\033[0m").strip()
        auth_data = authenticate(account, password)
        if auth_data:  # 已经拿到账户数据
            user_obj["is authenticated"] = True
            user_obj['data'] = auth_data
            print("welcome %s" % account)
            # 记录日志
            admin_logger.info("Super user %s logged in" % user_obj['data']['username'])
            # 开始具体功能
            controller(user_obj)
        else:
            print("wrong usename 或者 password")
            retry += 1
        if retry == 3:
            error_message = "你已经尝试了3次错误的用户名密码！"
            print(error_message)
            # 记录日志
            break