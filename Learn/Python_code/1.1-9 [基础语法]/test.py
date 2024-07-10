print("hellow world")
print("hellow")
print("hello world")

# 打印字面量
print("hellow world")
# 这是一行直接注释
# 这是一行注释，需要空格
# 这是一行正确注释
"""
这是多行注释
"""

# 给变量money赋值
money = 10
print("傻逼没钱了，还剩：", money, "块钱")
# 将内含变量的表达式赋予给新变量并使用print语句输出
money = money - 5
print("买完了冰激凌还剩：", money)
# 使用print（）输出类型信息type()表达式
print(type(114514))
# 使用变量存储type()语句的结果
int_type = type("114.14")
print(int_type)
# 使用type语句查看变量中存储的数据类型
nam = "我超，op"
str_type = type(nam)
print(str_type)
op = 114514
float_op = type(op)
print("op")
print(float_op)
# 使用转义字符串
print("\"转义字符\"")
# 字符串占位完成拼接
nam = ("sb%s") % (1114514)
print(nam)
op = 114514
sb = "我"
ooooh = "我超，%s%s" % (sb,op)
print(ooooh)

# 格式化表达式
print("我的名字是：%s" % "name=aa")
print(f"我的名字是：{1+1}")
nam1 = 5
nam2 = 2
nam3 = f"{nam2**nam1}"
print("""2的5次方是：%s" % nam3
""")

# # 初次使用if语句
# age = input("请输入年龄：")
# if age>= 18
#     print("您已成年，祝您游玩愉快")


# input语句的使用学习
# input("请随意输入：")
# print(input)

# while循环语句
# 输出50次666
"""i = 0
while i < 45:
    print(666)
    i += 1"""
# 输出从1加到100的和
n = 1
sum = 0
while n <= 100:
    sum += n
    n += 1
print(n)
print(sum)

print(type("class"))


# 复习99乘法表
n = 0
i = 0
while n <= 8:
    n += 1
    for i in range(1, n+1):
        print(f"{n}*{i}={n*i}\t",end='')
    print()


# test
int bibi = 20
print(bibi)