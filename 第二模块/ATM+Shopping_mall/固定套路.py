
#
features=[
    ("查看账户信息",logics.view_account_info),
    ("取钱",logics.with_draw),
    ("还钱",logics.pay_back),
    ("转账",logics.transfer),
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
                features[choice][1](user_obj,access_logger=access_logger,transaction_logger=transaction_logger)

            else:
                print("值必须小于"+len(features)+"请重新输入！")
                continue
        if choice=="q":exit("Goodbye")


#features是将让用户选择,从而执行相应的函数
#1.写一个list
#2. for index,feature in enumerate(features): 打印出来
#3. input ,让用户输入编号,features[choice][1]() 就直接执行了函数

# 注意要想使用feature这种套路，尽量他们在函数调用时参数的个数都一样，
# 这句就是对应功能的调用：features[choice][1](user_obj,access_logger=access_logger,transaction_logger=transaction_logger)


#套路2:
#atm_serve.py
if __name__ == "__main__":
    from atm import admin
    admin.entrance()
#写一个程序时,这个py文件就是就是启动程序文件。

