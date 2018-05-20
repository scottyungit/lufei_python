# encoding: utf-8
##购物车程序
import os
import json

#用到的日志文件
if not os.path.exists('shopping_car.json'):
    with open('shopping_car.json','x') as f:
        json.dump([],f)

if not os.path.exists('balance.txt'):
    f=open('balance.txt','x')
    f.close()
with open('shopping_car.json','r') as f1:
    shopping_car=json.load(f1)
with open('balance.txt','r') as f2:
    balance=f2.read().rstrip()

#商品列表
goods = [
{"name": "电脑", "price": 1999},
{"name": "鼠标", "price": 10},
{"name": "游艇", "price": 20},
{"name": "美女", "price": 998},
]
real_user_info={'scott':'123'}
username = input("enter your username: ")
password = input("enter your password: ")

#登陆认证
if (username,password) in real_user_info.items():
    if balance == '':
        salary=int(input("enter your salary: "))
        balance=salary
    else:
        balance=int(balance)
    print("---提供购买的商品列表是：")
    for index, p in enumerate(goods):
        print(index, p['name'], p['price'])
else:
    exit()

#查看购买历史纪录
ask_history=input("---你想要查看购买的历史纪录吗(yes/no)? ")
if ask_history == "yes":
    if shopping_car:
        for index,p in enumerate(shopping_car):
            print(index,p[0],p[1])
    else:
        print("you didn't buy anthing recently")
#开始购买
while True:
    index = input("请输入你想购买的商品编号: ")
    if index.isdigit():
        index=int(index)
        if index>=  0 and index<=3:
            print("Price",goods[index]['price'])
            if balance-(goods[index]['price'])>=0:
                #加入商品到购物车，并更新余额和商品到文件中
                shopping_car.append([goods[index]['name'],goods[index]['price']])
                print('\033[1;31;40m'+goods[index]['name']+"已经加入购物车"+"\033[0m")
                with open('shopping_car.json','w') as f1:
                    json.dump(shopping_car,f1)
                balance-=goods[index]['price']
                with open('balance.txt','w') as f2:
                    f2.write(str(balance))
            else:
                print('\033[1;31;40m'+"余额已不足，余:"+str(balance)+"\033[0m")
        else:
            print("商品不存在")
    elif index == 'q':
        if len(shopping_car)==0:
            print("you didn't buy anything.")
            break
        print("---您已经购买的商品是: ")
        for index,p in enumerate(shopping_car):
            print(index,p[0],p[1])
        print('\033[1;31;40m' + '---您的余额是: ' + str(balance) + "\033[0m")
        break

