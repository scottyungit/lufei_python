#-*- coding:utf-8 -*-
import json,os
from conf import settings

def save_db(account_data):
    account_file = os.path.join(settings.DB_ACCOUNTS_PATH, "%s.json" % account_data['username'])
    #print(account_file)
    # 这里需要思考，其实完全可以json.dump将user_obj['data']写入db文件中，但这样会覆盖掉源db文件，
    # 假设出现断电情况，会导致文件丢失，所以最好创建一个新的db文件，json.dump以后在os.rename过来。
    f = open(account_file + ".new", 'w',encoding="utf-8")
    json.dump(account_data, f)
    f.close()
    os.remove(account_file)
    os.rename(account_file + ".new", account_file)

def save_credit_card_db(account_data):
    account_file = os.path.join(settings.CREDIT_CARD_ACCOUNTS_PATH, "%s.json" % account_data['id'])
    #print(account_file)
    # 这里需要思考，其实完全可以json.dump将user_obj['data']写入db文件中，但这样会覆盖掉源db文件，
    # 假设出现断电情况，会导致文件丢失，所以最好创建一个新的db文件，json.dump以后在os.rename过来。
    f = open(account_file + ".new", 'w',encoding="utf-8")
    json.dump(account_data, f)
    f.close()
    os.remove(account_file)
    os.rename(account_file + ".new", account_file)

def load_account_data(account):
    """从文件里读出数据"""
    account_file = os.path.join(settings.DB_ACCOUNTS_PATH, "%s.json" % account)
    if os.path.isfile(account_file):   #判断一个PATH是不是一个文件。是就为True
        f=open(account_file,encoding="utf-8")
        data=json.load(f)
        f.close()
        return {"status":0,"data":data}
    else:
        return {"status":-1,"error":"The accounts file is not exists"}

# def load_good_data():
#     good_file = settings.DB_GOODS_PATH
#     if os.path.isfile(good_file):  # 判断一个PATH是不是一个文件。是就为True
#         f = open(good_file)
#         data = json.load(f)
#         f.close()
#         return {"data": data}
#     else:
#         return {"error": "The goods file is not exists"}