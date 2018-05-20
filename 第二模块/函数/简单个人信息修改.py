#coding:utf-8
def print_info(person):
    # print(type(int(person[3])),type(int(person[5])))
    # print(person[2],person[3],person[4],person[5])
    info = """ --------
    Name:  %s
    Age:   %s
    Job:   %s
    Phone: %s
    ---------""" % (person[2], person[3], person[4], person[5])
    print(info)


def change_info(person):
    for index, value in enumerate(person):
        if index == 2:
            print(str(index) + ". " + "Name: " + value)
        if index == 3:
            print(str(index) + ". " + "Age: " + value)
        if index == 4:
            print(str(index) + ". " + "Job: " + value)
        if index == 5:
            print(str(index) + ". " + "Phone: " + value)
    choice2 = input("please enter which part you want to change: ")
    print("当前值：" + person[int(choice2)])
    person[int(choice2)] = input("新值：")


def person_data():
    f=open('accounts.txt','r+')
    f_data=f.readlines()
    for line in f_data:
        line=line.rstrip()
        person=line.split(",")
        print(person)
        #print(person[0])
        def authorization():
            time=1
            while time<=3:
                time=1
                username=input("please enter username: ")
                password=input("please enter password: ")
                if username==person[0] and password==person[1]:
                    while True:
                        print("1.","打印个人信息")
                        print("2.","修改个人信息")
                        print("3","修改密码")
                        choice=input(">>>").strip()
                        if choice=="1":
                            print_info(person)
                        if choice=="2":
                            change_info(person)

        authorization()

person_data()