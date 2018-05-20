import os,sys
import json
from conf  import settings
from atm.db_handler import make_transaction,load_account_data
from utils  import util

@util.login
def view_account_info(user_obj,access_logger,transaction_logger):
    """
    1.打印用户信息，去除敏感信息
    :param user_obj: 
    :param access_log:
    :param transaction_log: 
    :return: 
    """
    print("below is the accounts info".center(50,'-'))
    #print(user_obj['data'])
    for k,v in user_obj['data'].items():
        if k not in "password":
            print("%15s:%s" %(k,v))
    print("END".center(50,'-'))
    transaction_logger.info("accounts %s views the accounts info" %user_obj['data']['id'])

@util.login
def with_draw(user_obj,access_logger,transaction_logger):
    """提现:1.显示余额
    输入提现金额
    判断如果余额大于（输入值+提现费）：减钱--写入db文件  这一步调用了make_transaction函数
    小于的话， print("余额不足")
    """
    print("当前余额:%s" %user_obj['data']['balance'])
    back_flag=False
    while not back_flag:
        with_draw_amount = input("\033[1;31;40m" + "输入你想提现的金额(输入'b'返回)：" + "\033[0m").strip()
        if with_draw_amount.isdigit() and float(with_draw_amount) >0:
            with_draw_amount=float(with_draw_amount)
            #调用交易函数
            if with_draw_amount<user_obj['data']['balance']:
                transaction_result=make_transaction(user_obj,"with_draw",with_draw_amount,transaction_logger)
                if transaction_result['status']==0:
                    print("\033[42;1m新的余额:%s\033[0m" %user_obj['data']['balance'])
                else:
                    print(transaction_result)
            else:
                print("\033[42;1m余额不足,当前余额:%s\033[0m" %user_obj['data']['balance'])
        elif with_draw_amount=="b":
            back_flag=True
        else:
            print("\033[42;1m输入不正确，请重新输入一个大于0数字\033[0m")

@util.login
def pay_back(user_obj,access_logger,transaction_logger):
    print("\033[42;1m当前余额:%s\033[0m" % user_obj['data']['balance'])
    back_flag = False
    while not back_flag:
        pay_back_amount = input("\033[1;31;40m" + "输入你想归还的金额(输入'b'返回):" + "\033[0m").strip()
        if pay_back_amount.isdigit() and float(pay_back_amount) > 0:
            pay_back_amount = float(pay_back_amount)
            # 调用交易函数
            transaction_result = make_transaction(user_obj, "pay_back", pay_back_amount, transaction_logger)
            if transaction_result['status'] == 0:
                print("\033[42;1m新的余额:%s\033[0m" % user_obj['data']['balance'])
            else:
                print(transaction_result)
        elif pay_back_amount == "b":
            back_flag = True
        else:
            print("\033[42;1m输入不正确，请重新输入一个大于0数字\033[0m")

@util.login
def transfer(user_obj,access_logger,transaction_logger):
    """
    1.输入对方account，调用load_account_data函数判断账户文件存在，并将账户数据存到dict
    2.输入转账金额，
    :param user_obj:
    :param access_logger:
    :param transaction_logger:
    :return:
    """
    print("\033[42;1m当前余额:%s\033[0m" % user_obj['data']['balance'])
    while True:
        transfer_account = input("\033[1;31;40m 输入对方账户: \033[0m").strip()
        account_data = load_account_data(transfer_account)
        if account_data['status'] == 0:
            account_data = account_data['data']
            break
        else:
            print("\033[42;1m请重新输入正确的account\033[0m")
            continue
    back_flag = False
    while not back_flag:
        transfer_amount = input("\033[1;31;40m" + "输入转账金额(输入'b'返回)：" + "\033[0m").strip()
        if transfer_amount.isdigit() and float(transfer_amount) > 0:
            transfer_amount = float(transfer_amount)
            # 调用交易函数
            transaction_result = make_transaction(user_obj, "transfer", transfer_amount, transaction_logger,account_data)
            if transaction_result['status'] == 0:
                print("\033[42;1m新的余额:%s\033[0m" % user_obj['data']['balance'])
            else:
                print(transaction_result['error'])
        elif transfer_amount == "b":
            back_flag = True
        else:
            print("\033[42;1m输入不正确，请重新输入一个大于0数字\033[0m")




