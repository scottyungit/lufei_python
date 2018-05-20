# encoding: utf-8
real_username = 'scott1'
real_password = 'password1'
i=1
while i <= 3:
    username = input("what's you username:")
    password = input("what's your password:")
    if username == real_username and password == real_password :
        print('welcome',username)
        exit()
    i+=1
