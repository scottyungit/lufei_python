# name=[1,2,3,4,5]
# count=0
# #enumerate枚举 能循环出找到索引值和对应的value
# for x in enumerate(name):
#     print(x)
#
# for x,y in enumerate(name):
#     if x%2==0:
#         name[x]=-1
#         #print(x,y)
# print(name)
#
# ###
# choice =input("please type product number you want to by:")
# if choice.isdigit():
#     choice=input(choice)
# elif choice == 'q':
#     print("...")


names=["scott1",'scott2',3,'scott3','scott4',3,'scott5','scott6',3,'scott7']
print(names.index(3))
first_index=names.index(3)
new_list=names[first_index+1:]
sencond_list=new_list.index(3)
print(first_index+sencond_list+1)
