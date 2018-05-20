import json,os,sys
from conf import settings
#print(sys.path)

def load_credit_card_account_data(account):
    """从文件里读出数据"""
    account_file = os.path.join(settings.CREDIT_CARD_ACCOUNTS_PATH, "%s.json" % account)
    if os.path.isfile(account_file):   #判断一个PATH是不是一个文件。是就为True
        f=open(account_file,encoding="utf-8")
        data=json.load(f)
        f.close()
        return {"status":0,"data":data}
    else:
        return {"status":-1,"error":"The accounts file is not exists"}


def authenticate_credit_card(account,password):
    """对用户信息进行验证"""
    account_data=load_credit_card_account_data(account)
    if account_data["status"] == 0:  #账户文件加载成功
        account_data=account_data['data']
        if password == account_data["password"]:  #为什么没验证account id,很简单，之前能load_account_data，就说明id文件有了
            if account_data['status']==-1:
                print("此用卡帐户已冻结,强制退出")
                #exit()
            else:
                return account_data
        else:
            return None
    else:
        #print(account_data['error'])
        return None


def load_atm_user_obj_data(atm_user_obj,access_logger):
    retry=0
    while  atm_user_obj["is authenticated"] is not True:
        account = input("please enter your account: ").strip()
        password = input("please enter your password: ").strip()
        auth_data = authenticate_credit_card(account, password)
        if auth_data:  # 已经拿到账户数据
            atm_user_obj["is authenticated"] = True
            atm_user_obj['data'] = auth_data
            print("\033[42;1m信用卡验证成功\033[0m")
            # 记录日志
            access_logger.info("user %s logged in" % atm_user_obj['data']['id'])
            # 开始具体功能

        else:
            print("wrong account or password.Authenticating Failed!")
            retry += 1
        if retry == 3:
            error_message = "你已经尝试了3次错误的用户名密码,无法继续！"
            print(error_message)
            exit()