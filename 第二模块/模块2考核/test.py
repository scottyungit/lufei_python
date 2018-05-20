# a=[ x for x in range(10) ]
# aa = 2 if 2>5 else 5
# print(aa)

#
# f=open("test1.txt","r")
# sum=0
# for line in f:
#     line=line.strip()
#     #print(line)
#     l=line.split()
#     print(l)
#     brand=l[0]
#     ji=int(l[1])*int(l[2])
#     sum+=ji
# print(sum)

def timmer(func):
    def wrapper(*args):
        t1 = time.time()
        func(*args)
        t2=time.time()
        print(t2-t1)
    return wrapper



import time
@timmer  #func=timmer(func)
def func():
    time.sleep(5)


func()

