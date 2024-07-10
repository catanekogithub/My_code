# 1
print("""说明：请在1-30之间猜测一个数字，您有4次机会""")

# 建立一个随机数赋予给变量num
import random
num = random.randint(1, 30)
# 使用if语句
# 第一次输入
n = 1
guess_num = int(input("请输入数字："))
while n <= 4:
    if guess_num == num:
        if n == 1:
            print("第一次就猜对了，什么欧皇")
        else:
            print(f"恭喜你第{n}次猜对啦~")
        break
    else:
        if n == 4:
            print("都猜错啦，游戏结束")
        else:
            if guess_num > num:
                print("猜大了捏")
            else:
                print("猜小了捏")
            guess_num = int(input("请再次输入数字："))
        n += 1
input("回车键退出：")
