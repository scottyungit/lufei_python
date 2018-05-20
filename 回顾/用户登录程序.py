# /usr/bin/env python
# encoding: utf-8


time = 0
while time < 3:
    username = input("please enter your name:")
    password = input("please enter your password:")
    if username == "scott" and password == "123":
        print("welcome %s %(username)")
        exit(0)
    else:
        time+=1
else:
    print("超过三次失败")

