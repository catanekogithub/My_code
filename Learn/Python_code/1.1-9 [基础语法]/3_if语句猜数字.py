# 初次使用if语句，使用if elif else语句制作猜数字小游戏
print("""猜数字小游戏
说明：在0-20间猜出某一数字，您有3次机会~
     """)
# 定义一个随机数
import random
number = random.randint(0, 20)
guess_1 = float(input("请输入数字："))
if guess_1 == number:
    print("正确")
else:
    if guess_1 > number:
        print("猜大了")
    else:
        print("猜小了")
guess_2 = int(input("再来一次："))
if guess_2 == number:
    print("正确")
else:
    if guess_2 > number:
        print("猜大了")
    else:
        print("猜小了")
guess_3 = int(input("再来一次："))
if guess_3 == number:
    print(f"正确,答案为{number}")
else:
    print(f"都错啦，答案是{number}")
