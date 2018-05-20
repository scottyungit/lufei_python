#双分支 if-else
#多分支 if-elif-else

# while True:
#     score = int(input("score:"))
#     if score > 100 or score < 0:
#         print("Out")
#         break
#     if score <= 100 and score >= 90:
#         print("A")
#     elif score >= 80:
#         print("B")
#     elif score >> 70:
#         print("C")
#     else:
#         print("D")

#打印偶数
# count = 0
# count_even=[]
# count_odd=[]
# while count <= 100:
#     if count % 2 == 0:
#         count_even.append(count)
#     elif count % 2 == 1:
#         count_odd.append(count)
#     count += 1
# print(count_even)
# print(count_odd)

#while-else：当循环正常执行完，没有被break过的话，就会执行else的语句
#上面的代码加入break和else测试结果
count = 0
count_even=[]
count_odd=[]
while count <= 100:
    if count % 2 == 0:
        count_even.append(count)
    elif count % 2 == 1:
        break
    count += 1
else:
    print("code ok")
print(count_even)
print(count_odd)



