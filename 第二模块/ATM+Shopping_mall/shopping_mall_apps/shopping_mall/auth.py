from .db_handler import  load_account_data

def authenticate(account,password):
    "对用户信息进行验证"
    account_data=load_account_data(account)
    if account_data["status"] == 0:  #账户文件加载成功
        account_data=account_data['data']
        if password == account_data["password"]:  #为什么没验证account id,很简单，之前能load_account_data，就说明id文件有了
            if account_data['status'] == -1:
                print("帐户已冻结,强制退出")
                exit()
            else:
                return account_data
        else:
            return None
    else:
        #print(account_data['error'])
        return None
