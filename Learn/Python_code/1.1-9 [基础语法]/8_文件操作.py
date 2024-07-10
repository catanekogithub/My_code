

# 数据文件的读取与写入综合案例
# 以只读和写入模式打开两个文件
fw = open("D:\Program File\My-Code\Learn\TEMP\text copy.txt",
     "r", encoding='UTF-8')
f = open("D:\Program File\My-Code\Learn\TEMP\text.txt",
     "r", encoding='UTF-8')
for x in f:
    x.split(",", )