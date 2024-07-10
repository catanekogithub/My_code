# 1
print("""说明：请在1-10之间随机猜测一个数字""")
# 建立一个随机数赋予给变量num
import random
num = random.randint(1,10)
# 使用if语句
flag = True
n = 0
while flag:
    guess_num = int(input("请输入数字："))
    n += 1
    if guess_num == num:
        if n == 1:
            print("恭喜你第一次就猜对啦~")
        else:
            print("恭喜你猜对啦~")
            print(f"""您一共猜了{n}次""")
        flag = False
    else:
        if guess_num > num:
            print("猜大了")
        else:
            print("猜小了")
input("输入任意键退出：")

