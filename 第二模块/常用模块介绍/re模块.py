f=open("re_file.txt",encoding="utf-8")
#默认循环实现
phones=[]
for line in f.readlines():
    name,city,height,weight,phone=line.rstrip().split()
    print(phone)
    phones.append(phone)

print(phones)
f.close()

#re模块
import re
f=open("re_file.txt",encoding="utf-8")
data=f.read()
f.close()
phones2=re.findall("[0-9]{11}",data)
print(phones2)