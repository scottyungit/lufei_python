#-*- coding:utf-8 -*-
import json,os
from .db_handler import  save_db,save_credit_card_db
from utils.util import login

def view_shopping_info(user_obj,atm_user_obj,good_obj,access_logger,transaction_logger):
    if user_obj['data']['shopping_cart']:
        for index,p in enumerate(user_obj['data']['shopping_cart']):
            print("\033[42;1m%s %s %s\033[0m" %(index, p['name'], p['price']))
    else:


@login
def add_shopping_cart(user_obj,atm_user_obj,good_obj,access_logger,transaction_logger):
    print("---提供购买的商品列表是：")
    for index, p in enumerate(good_obj):
        print("\033[42;1m%s %s %s\033[0m" %(index, p['name'], p['price']))

    # 已经购买的商品
    while True:
        index = input(">>>请输入你想购买的商品编号(输入'b'返回上): ")
        if index.isdigit():
            index = int(index)
            if index >= 0 and index <= len(good_obj):
                old_balance=atm_user_obj['data']['balance']
                if old_balance - (good_obj[index]['price']) >= 0:
                    # 加入商品到购物车，并更新余额和商品到文件中
                    user_obj['data']['shopping_cart'].append({"name":good_obj[index]['name'], "price":good_obj[index]['price']})
                    print('\033[1;31;40m' + good_obj[index]['name'] + "已经加入购物车" + "\033[0m")
                    atm_user_obj['data']['balance']=old_balance-good_obj[index]['price']
                    save_db(user_obj['data'])
                    save_credit_card_db(atm_user_obj['data'])
                    transaction_logger.info("accounts：%s tran_type:shopping action:minus amount:%s  balance:%s"
                                            % (atm_user_obj['data']['id'],good_obj[index]['price'],atm_user_obj['data']['balance']))

                else:
                    print('\033[1;31;40m' + "余额已不足，余:" + str(old_balance) + "\033[0m")
            else:
                print("商品不存在")
        elif index == 'b':
            if len(user_obj['data']['shopping_cart']) == 0:
                print("you didn't buy anything.")
                break
            print("---您总共购买的商品是: ")
            for index, p in enumerate(user_obj['data']['shopping_cart']):
                print(index, p["name"], p['price'])
            print('\033[1;31;40m' + '---您的余额是: ' + str(atm_user_obj['data']['balance']) + "\033[0m")
            break



