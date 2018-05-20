# encoding: utf-8
##购物车程序
goods = [
{"name": "电脑", "price": 1999},
{"name": "鼠标", "price": 10},
{"name": "游艇", "price": 20},
{"name": "美女", "price": 998},
]

real_user_info={'scott':'123'}
username = input("enter your username: ")
password = input("enter your password: ")
if (username,password) in real_user_info.items():
    salary=int(input("enter your salary: "))
    print("---您可以购买的商品列表是：")
    for index,p in enumerate(goods):
        print(index, p['name'], p['price'])
else:
    exit()

shopping_car=[]
balance=salary
#开始购买
while True:
    index = input("please enter the number you want: ")
    if index.isdigit():
        index=int(index)
        if index >= 0 and index <= 3:
            if balance-(goods[index]['price'])>=0:
                #商品加入到购物车
                shopping_car.append([goods[index]['name'],goods[index]['price']])
                print('\033[1;31;40m' + goods[index]['name'] + "已经加入购物车" + "\033[0m")
                balance -= goods[index]['price']
            else:
                print('\033[1;31;40m'+"余额已不足，余:"+str(balance)+"\033[0m")
        else:
            print("商品不存在")

    #退出，打印商品和余额
    if index == 'q':
        if len(shopping_car)==0:
            print("you didn't buy anything.")
            break
        print("---您已经购买的商品是：")
        for index, p in enumerate(shopping_car):
            print(index,p[0],p[1])
        print('\033[1;31;40m'+'---您的余额是: '+str(balance)+"\033[0m")
        break
