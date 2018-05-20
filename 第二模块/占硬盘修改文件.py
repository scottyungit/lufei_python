#encoding : utf-8
import  os
f_name='文件2.txt'
f_new_name=f_name+".new"
print(f_new_name)

f=open(f_name,'r+')
f_new=open(f_new_name,'w')
for line in f:
    line=line.replace("hello","你好")
    f_new.write(line)
f.close()
f_new.close()

os.replace(f_new_name,f_name)