# encoding: utf-8
import os
# if not os.path.exists('lock_user'):
#     f=open('lock_user','x')
#     f.close
f=open('lock_user','r')
lock_user=f.read()
print("locker_user",lock_user)
f.close()
real_user_info = {'scott1':'password1','scott2':'password2','scott3':'password3'}
i=1
while i<=3:
        username = input("what's you username:")
        password = input("what's your password:")
        #在黑名单中，直接退出
        if username == lock_user:
            print("您之前尝试密码次数过多，已被禁用")
            exit(1)
        #检查用户名密码
        if (username,password) in real_user_info.items():
            print('欢迎',username)
            exit(0)
        i+=1
else:
    #三次错误，加入黑名单
    f=open('lock_user','a')
    f.write(username)
    f.close()
    print("%s 被加入黑名单" %(username))
    exit(1)