#-*- coding: utf-8 -*-
import os
def select():
    """查询语句1：find name,age from staff_table where age >= 22
            2: find * from staff_table where dept = IT
            3：find * from staff_table where enroll_date like 2013"""
    sql=input("输入查询语句： ")
    sql_list=sql.strip().split()
    staff_table_var_list = ["staff_id", "name", "age", "phone", "dept", "enroll_date"]
    where_var_index=staff_table_var_list.index(sql_list[5])
    #对select 查询的字段进行处理
    def print_select_var():
        if sql_list[1]=="*":
            print(lines)
        else:
            find_var_list = sql_list[1].split(",")
            select_value = []
            for var in find_var_list:
                result = line_list[staff_table_var_list.index(var)]
                print(result, end=" ")
            print()
    i=0
    f = open("staff_table.txt", "r", encoding="utf-8")
    for line in f:
        lines=line.strip()
        line_list=line.strip().split(",")
        #where 字段匹配
        if sql_list[6] == ">=":
            if int(line_list[where_var_index])>=int(sql_list[7]):
                i+=1
                print_select_var()
        if sql_list[6] == "=":
            if line_list[where_var_index] == sql_list[7]:
                i+=1
                print_select_var()

        if sql_list[6] == "like":
            if line_list[where_var_index].split("-")[0] in sql_list[7]:
                i+=1
                print_select_var()
    print("\033[1;31;40m"+"查询成功，影响了"+str(i)+"条记录"+"\033[0m")


def add():
    """添加语句：Alex Li,22,13651054608,IT,2013-04-01"""
    sql = input('输入员工信息(姓名，年龄，电话，部门，日期)：').strip()
    sql_list=sql.split(",")
    f=open("staff_table.txt",'r',encoding="utf-8")
    phone_list=[]
    data_all = []
    for line in f:
        #staff_id=line.strip().split(",")[0]
        phone=line.strip().split(",")[3]
        phone_list.append(phone)
    if sql_list[2] in phone_list:
        print("手机号已经存在了！")
        f.close()
    else:
        f2 = open("staff_table.txt", 'r+', encoding="utf-8")
        for line2 in f2.readlines():
            data_all.append(line2.rstrip())
        #print("data_all:",data_all)
        add_staff_id=str(len(data_all)+1)
        sql_list.insert(0,add_staff_id)
        new_record=",".join(sql_list)
        f2.write("\n"+new_record)
        f2.flush()
        f2.close()
        print("添加成功")

def remove():
    """语法： del from staff_table.txt  where id = 3"""
    staff_id=input("输入删除员工语句: ")
    staff_id=staff_id.strip().split()[-1]
    f=open("staff_table.txt","r")
    f1=open("staff_table2.txt","a")
    for line in f:
        line_list=line.split(",")
        line_id=line_list[0]
        if int(line_id)<int(staff_id):
            f1.write(line)
            f1.flush()
        elif int(line_id)>int(staff_id):
            line_list[0]=str(int(line_list[0])-1)
            f1.write(",".join(line_list))
        else:
            continue
    f.close()
    f1.close()
    os.remove("staff_table.txt")
    os.rename("staff_table2.txt","staff_table.txt")
    print("删除成功")

def change():
    """
    输入语句： Update staff_table.txt set dept = Market where dept = IT
               Update staff_table.txt set age = 25      where name = Alex Li
    """
    sql=input("输入你想要改变的信息：")
    sql_list=sql.strip().split()
    staff_table_var_list=["staff_id","name","age","phone","dept","enroll-date"]
    set_var_index=int(staff_table_var_list.index(sql_list[3]))
    where_var_index=int(staff_table_var_list.index(sql_list[7]))
    #取出where中变量的值，这里多这一步，防止字段值中有空格，选择"="取值
    where_var_index_value=sql.split("=")[-1].strip()
    f=open("staff_table.txt","r",encoding="utf-8")
    f1=open("staff_table2.txt","w",encoding="utf-8")
    res=0
    for line in f:
        lines=line.strip()
        line_list=line.strip().split(",")
        #where语句匹配，然后修改字段
        if line_list[where_var_index] == where_var_index_value:
            lines=lines.replace(line_list[set_var_index],sql_list[5])
            res+=1
        f1.write(lines+"\n")
    f.close()
    f1.close()
    os.remove("staff_table.txt")
    os.rename("staff_table2.txt","staff_table.txt")
    print("\033[1;31;40m"+"修改成功，影响了"+str(res)+"条记录"+"\033[0m")

messages="""
1:select
2:add
3:remove
4:change
5.exit
"""
messages_dict={"1":select,"2":add,"3":remove,"4":change,"5":"exit"}
#开始
while True:
    print(messages)
    choice = input('你想要执行什么操作:')
    if not choice or choice not in messages_dict:continue
    if choice=="5":break
    messages_dict[choice]()

