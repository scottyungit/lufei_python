import os,sys,datetime
import json
from conf  import settings
#from atm.db_handler import make_transaction,load_account_data
from utils_admin import util

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

@util.login
def add_account(user_obj,admin_logger):
    back_flag = False
    while not back_flag:
        new_account=input("\033[1;31;40mplease enter the new accounts id(Enter 'b' for back)：\033[0m").strip()
        if new_account.isdigit() and int(new_account) >0:
            account_file = os.path.join(settings.DB_ACCOUNTS_PATH, "%s.json" % new_account)
            if os.path.isfile(account_file):  # 判断一个PATH是不是一个文件。是就为True
                print("The accounts file is already exists")
            else:
                credit=float(input("Enter credit: ").strip())
                balance=credit
                expire_date=input("Enter the expire date:(格式如:2020-01-01) ").strip()
                enroll_date=datetime.datetime.now().strftime("%Y-%m-%d")
                id=int(new_account)
                status=0
                password=input("Enter the password: ")
                account_data={"balance":balance,"expire_date":expire_date,"enroll_date":enroll_date,"credit":credit,"id":id,"password":password,"status":status}
                f=open(account_file,'w')
                json.dump(account_data,f)
                if os.path.isfile(account_file):
                    print("添加帐户成功")
                    admin_logger.info("Super user:%s add new accounts:%s"  %(user_obj['data']['username'],account_data['id']))
        elif new_account=="b":
            back_flag = True
        else:
            print("输入不正确，请重新输入一个大于0数字")

@util.login
def add_credit(user_obj,admin_logger):
    back_flag = False
    while not back_flag:
        account = input("\033[1;31;40mplease enter the accounts id(Enter 'b' for back)：\033[0m").strip()
        if account.isdigit() and int(account) > 0:
            account_data=load_account_data(account)
            if account_data['status']==0:
                account_data=account_data['data']
                current_credit = account_data['credit']
                print("\033[42;1m当前信用额度:%s\033[0m" % current_credit)
                upgrade_credit = input("\033[1;31;40mplease add a credit value：\033[0m").strip()
                if upgrade_credit.isdigit() and float(upgrade_credit) > 0:
                    new_credit = float(upgrade_credit) + current_credit
                    account_data['credit'] = new_credit
                    save_db(account_data)
                    print("修改额度成功,新的额度%s" % new_credit)
                    admin_logger.info(
                        "Super user:%s operation type:add credit operation accounts:%s  new credit value:%s" % (
                        user_obj['data']['username'], account_data['id'],
                        account_data['credit']))
                else:
                    print("输入不正确，请重新输入一个大于0数字")
            #account_file = os.path.join(settings.DB_ACCOUNTS_PATH, "%s.json" % accounts)
            #if not os.path.isfile(account_file):  # 判断一个PATH是不是一个文件。是就为True
            #    print("The accounts file is not exists")
            #    continue
            else:
                print(account_data['error'])
        elif account == "b":
            back_flag = True
        else:
            print("输入不正确，请重新输入一个大于0数字")

@util.login
def froze_account(user_obj,admin_logger):
    back_flag = False
    while not back_flag:
        account = input("\033[1;31;40mplease enter the accounts id(Enter 'b' for back)：\033[0m").strip()
        if account.isdigit() and int(account) > 0:
            account_data=load_account_data(account)
            if account_data['status']==0:
               account_data=account_data['data']
               current_status = account_data['status']
               if current_status == 0:
                   upgrade_status = input("\033[1;31;40mWould you like to change the status(yes/no,default:yes)：\033[0m").strip()
                   if upgrade_status == "" or upgrade_status == "yes":
                       print("in if --yes value", upgrade_status)
                       new_status = -1
                       account_data['status'] = -1
                       save_db(account_data)
                       print("帐户冻结成功" )
                       admin_logger.info(
                       "Super user:%s operation type:frozen accounts operation accounts:%s  new status value:%s" % (
                           user_obj['data']['username'], account_data['id'],
                           account_data['status']))
               else:
                   print("当前帐户已被冻结")
            else:
               print(account_data['error'])

        elif account == "b":
            back_flag = True
        else:
            print("输入不正确，请重新输入一个大于0数字")