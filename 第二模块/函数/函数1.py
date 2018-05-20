# encoding:utf-8
def sayhi(x,y):
    print("hello",x,"I'm",y)

sayhi("scott","leijie")

#函数的参数
#默认参数 :默认参数放在最后
def stuent(name,age,country="CN")
#关键字参数，就是在调用时，指出形参=实参。明确表示了！ 要求：关键参数放在位置参数之后
调用： student("scott",age=25,country="CN")

#非固定参数 *args （元祖）   **kwargs （字典）
def alert(msg,*users,**kwargs)
    