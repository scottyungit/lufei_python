# # # name1='scott'
# # # name2='scott'
# # # print (name1) if name1 is name2 else print("different")
# # #
# # #
# # # i=0
# # # while i<=3:
# # #     user=input("what's you username:")
# # #     password=input("what's your password:")
# # #
# # #     if (user=='seven'or user=='alex') and password=='123':
# # #         print("successful login!")
# # #         break
# # #     else:
# # #         print("failed login!")
# # #         i=i+1
# # #学习if
# # gender=input("gender:")
# # age=int(input("age:"))
# # if gender == '女':
# #     if age <28:
# #         print("I love girls")
# #     else:
# #         print("姐弟恋很好")
# # else:
# #     print("搞基吧")
#
# # s="""11,alex li,25,13698424613,IT,2015-10-29
# # 11,alex wang,25,13698424614,IT,2015-10-30"""
# # #以行作为分隔符（如果不指定）
# # print(s.splitlines())
# # print(",".join(s.splitlines()))
#
# a=[1,10]
# def plus(a):
#     a.append(100)
#     print(a)
# plus(a)
#
# print(a)


f=open("hosts","r")
fp=f.readlines()
line_list=[]
for line in fp:
    line=line.strip()
    s=line.split()
    print(s)

