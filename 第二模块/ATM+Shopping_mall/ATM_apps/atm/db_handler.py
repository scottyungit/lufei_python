#-*- coding:utf-8 -*-
import json,os
from conf import settings

def save_db(account_data):
    account_file = os.path.join(settings.DB_ACCOUNTS_PATH, "%s.json" % account_data['id'])
    #print(account_file)
    # 这里需要思考，其实完全可以json.dump将user_obj['data']写入db文件中，但这样会覆盖掉源db文件，
    # 假设出现断电情况，会导致文件丢失，所以最好创建一个新的db文件，json.dump以后在os.rename过来。
    f = open(account_file + ".new", 'w')
    json.dump(account_data, f)
    f.close()
    os.remove(account_file)
    os.rename(account_file + ".new", account_file)

def load_account_data(account):
    """从文件里读出数据"""
    account_file = os.path.join(settings.DB_ACCOUNTS_PATH, "%s.json" % account)
    if os.path.isfile(account_file):   #判断一个PATH是不是一个文件。是就为True
        f=open(account_file)
        data=json.load(f)
        f.close()
        return {"status":0,"data":data}
    else:
        return {"status":-1,"error":"The accounts file is not exists"}

def make_transaction(user_obj,tran_type,amount,transaction_logger,transfer_account_data=None):
    amount=float(amount)
    old_balance = user_obj['data']['balance']
    if tran_type in settings.TRANSACTION_TYPE:
        interest=settings.TRANSACTION_TYPE[tran_type]['interest']*amount
        if settings.TRANSACTION_TYPE[tran_type]['action']=="plus":
            new_balance=old_balance+amount+interest
        elif settings.TRANSACTION_TYPE[tran_type]['action']=="minus":
            new_balance = old_balance - amount-interest
            if new_balance<0:
                print("\033[1;31;40m您的余额不够去支持这次交易[-%s]，您当前余额为为%s" % (amount+interest,old_balance))
                return {"status": -1,"error":"交易失败，余额不足"}
        elif  settings.TRANSACTION_TYPE[tran_type]['action']=="transfer":
            new_balance=old_balance-amount-interest
            if new_balance<0:
                print("\033[1;31;40m您的余额不够去支持这次交易[-%s]，您当前余额为为%s" % (amount+interest,old_balance))
                return {"status": -1,"error":"交易失败，余额不足"}
            transfer_account_balance=transfer_account_data['balance']+amount+interest
        # 新的余额记入内存
        user_obj['data']['balance'] = new_balance
        save_db(user_obj['data'])
        if transfer_account_data:
            transfer_account_data['balance']=transfer_account_balance
            save_db(transfer_account_data)
        #无论哪种操作类型类型，都需要将新的余额写入文件
        transaction_logger.info("accounts：%s tran_type:%s action:%s amount:%s interest:%s balance:%s"
                                %(user_obj['data']['id'],tran_type,settings.TRANSACTION_TYPE[tran_type]['action'],amount,interest,user_obj['data']['balance']))
        return {"status":0}

    else:
        print("没有此种交易类型")
        return{"status":-1,"error":"交易类型[%s]不存在" %tran_type}



