
# print()语句的使用
print("genshinstart")

# 这是一行注释,不会被当作程序执行
"""
这是一段多行注释
one
two
print("123")
"""


# 买冰激凌练习, 赋予自变量money一个值
money = 59
print("我有", money, "元", "买了一个冰激凌花了10元,还剩:", money - 10, "元")
print()

# 使用type()语句查看变量储存的数据类型并直接print结果
print("查看变量money储存的数据类型:", type(money))
# 赋予变量一个"由type语句返回的数据类型信息"
type_money = type(money)
print("查看变量type_money存储的数据类型信息;", type_money)# print出来
print()

# 字符串的拼接打印
str_type = "1234"
print("123" + str_type)
# 字符串格式化(精度控制)
print("我现在还剩下%.2f元" % money)
# 买冰激淋复习-结合字符串格式化
money = 30
icecream_price = 10
print("我有%.2f元,买了一个冰激凌花了%.2f元,还剩%.2f元" % (money, icecream_price, money - icecream_price))
# format语句快速格式化字面量
print(f"我有{money}元,买了一个冰激凌花了{icecream_price}元,还剩{money - icecream_price}元")

# 查看input语句返回的数据类型
#mimi = type(input("输入:"))
#print(f"input语句返回的数据数据类型为{mimi}")


# while语句复习1
i = 1
while i < 10:
    print(f"挣钱第{i}天")
    if i < 5:
        print(f"才第{i}天,还没到第五天,继续")
    else:
        print(f"第{i}天了,离目标还剩{10 - i}天")
    i += 1
print(f"第{i}天了,坐牢结束")
print()

# while语句复习2-累加
n = 1
i = 0
while n <= 100:
    i += n
    n += 1
print(f"1累加到100的值为{i}")
print()

program_bool = True
# while语句猜测数字复习(无限次)
# import random
# num = random.randint(1,100)
# #
# print(f"guess a number which between 1-100")
# guess_num = float(input("please guess:"))
# while guess_num != num:
#     if guess_num < num:
#         print("the number is too small")
#     else:
#         print("the number is too big")
#     guess_num = float(input("try again:"))
# print("you are right!")

# 第四章_打印99乘法表_while循环
print(f"hello{money}", end='')
print("114514")
print("12\t4")
print("3\t3")

n = 1
while n <= 9:
    i = 1
    while i <= n:
        if i < n:
            print(f'{i}*{n}={n * i}\t', end='')
        else:
            print(f'{i}*{n}={n * i}\t')
        i += 1
    n += 1
print()

# for循环练习
name = "asdjfadfdasdsfadaewgaehathsahtahaaof"
number = 0
for test in name:
    if test == "a":
        number += 1
print(f"{name}中一共有{number}个字母a")
# for循环的覆盖探究
x = 0
for x in range(10):
    print(x)
print(x)
# for循环打印99乘法表
for x in range(1, 10):
    for y in range(1, x + 1):
        print(f"{x}*{y}={x * y}\t", end='')
    print()

# 快速格式化精度控制
test = 1234
print(f'快速格式化精度控制为小数点后两位:{test:.2f}')