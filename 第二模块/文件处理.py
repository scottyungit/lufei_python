#encoding:utf-8
#文件处理：
f=open("文件2.txt",mode="r",encoding="utf-8")
data=f.read()
f.close()
#mode=rb
#b就是2进制模式，不需要转成字符串。b存在的意义是什么呢？
#网络传输文件,视频文件等这些就可以使用b了
#chardet 模块是第三方工具，可以自动检测文件的编码。当你不知道文件是啥字符编码时，你可以用它帮你检测。

import  chardet
#1.先已rb模式打开文件
f=open("文件.txt",mode="rb")
data=f.read()
f.close()
#2.chardet.detect
chardet.detect(data)  #返回编码类型
print(chardet.detect(data))
#这样就结束了。当知道编码以后，可以解码成 unicode
#data.decode("gbk")  #从gbk解码成unicode.会显示出字符串。

#写模式
f=open("文件.txt",mode="w",encoding="utf-8")
f.write("写入文件")
f.close()
#二进制写入模式
f=open("文件.txt",mode="wb")
f.write("写入文件\n".encode("utf-8"))

#读写模式:先读再追加
f=open("文件.txt",mode="r+",encoding="utf-8")
data=f.read()
print(id(f.read()))
print("原内容:",data)
f.write("写入新内容\n")
f.write("新内容2\n")
print("新内容：",f.read())
f.close()

#python再执行文件，如写文件时，在你没有关闭文件（f.close()）时候,你写入到文件是在内存里边，你打开文件是看不见新写的内容。
#当你关闭的时候，内容才会更新。这是因为新写的内容是在内存里边（buffer），当buffer满了以后，才会更新到硬盘上。所以怎么让文件
#自动更新到硬盘上的？
#强制更新文件的方法：f.flush()
f=open("文件.txt",mode="w")
f.write("写入新内容\n")
#强制更新
f.flush()
f.close()

#判断是否可读
f.readable()
#读一行，每执行一次读一行内容,
f.readlines()
#返回当前光标的位置
f.tell()
#seek移动光标
f.seek()
#从光标所处位置（tell找到光标处）开始截断文件，后边跟上值以后：表示从0开始留下多少字节，后边的不要了
f.truncate()    #在读写模式下，才有意义

read方法 是读字符,seek,tell,truncate是读的字节

