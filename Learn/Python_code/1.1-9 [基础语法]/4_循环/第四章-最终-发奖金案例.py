# 20名员工依次发奖金,每人可领取1000元, 绩效不足仅可领取200元
money = 12000
i = 1
for i in range(1, 21):
    # 定义储存随机数的变量 n，代表员工绩效分
    import random
    n = random.randint(1, 10)
    # 检查余额
    print(f'company count rest {money}元')
    if money >= 200:
        # 检查员工是否符合条件
        if n < 5:
            money -= 200
            print(f"{i}员工因绩效分为{n}，未达标准，给200")
        else:
            if money >= 1000:
                money -= 1000
                print(f"{i}员工绩效分为{n}，meet the conditions，领取奖金1000元")
            else:
                print(f'''{i}员工绩效分为{n}，meet the conditions, 但账户余额不足以发放奖金
发放结束''')
                break
    else:
        print("奖金领完了，明年再说吧")
        break
if i == 20:
    print("所有员工领取完毕~")
else:
    if 21 - i >= 1:
        print(f'还剩{21 - i}名员工未处理')
    else:
        print('所有员工处理完毕~')

# 20名员工依次发奖金,每人可领取1000元
# i = 0
# money = 10000
# for i in range(1,21):
#     # 定义储存随机数的变量 n，代表员工绩效分
#     import random
#     n = random.randint(1,10)
#     # 员工不满足要求，使用continue跳过该员工，进入下一个员工循环
#     if n < 5:
#         print(f"{i}员工因绩效分为{n}，不足5，不给奖金")
#     # 检查余额
#     elif money >= 1000:
#         # 员工符合条件,发1000元
#         money -= 1000
#         print(f"{i}员工绩效分为{n}，满足条件，领取奖金1000元，账户还剩余{money}元")
#     else:
#         print("奖金领完了，明年再说吧")
#         break
#     if i == 20:
#         print("所有员工领取完毕~")







