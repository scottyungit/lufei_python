#while
count=1
while count<=10:
    if count==5:
        pass
    elif count>=6 and count <= 8:
        print(count**2)
    else:
        print(count)
    count+=1

with open('test.txt','a') as f:
    f.write("""
hello,word!
I'm scott!\n""")
