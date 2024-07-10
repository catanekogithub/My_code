
# 定义
def add(x, y, z):
    result = x + y + z
    print(f'{x}+{y}+{z}={result}')
    print(result)
# 调用
add(2, 1, 3)
# add(2, 1) 报错

print()
def check(x):
    # if x >= 6:
    #     print('you add a number >= 6')
    # else:
    #     print('this number < 6')
    return x + 1
# function reference
check(6)
# r = check(int(input(':')))
# print(r)

# print(pow(2,3,3))

# 小甲鱼课程函数学习
# def myfunc(name="defaultname"):
#      for r in range(3):
#          print(f"printname:{name}")

# def myfunc(name="defaultname", printtime=1):
#      for r in range(printtime):
#          print(f"printname:{name}")
# myfunc(114514, 2)

# def function_1(x, y,/, z):  # 定义一个函数 function_1
#     print(f"x是{x}, y是{y}, z是{z}")
# function_1(1,4,2)  # 执行结果为 {x是1, y是4, z是2}

# def myfunc(*args, printtime, args2="default"):
#      for r in range(printtime):
#          print(f"printargs:{args2}{args}")
# myfunc(2,6,1,2,1,1,1,printtime=2)

# type(kwrags) = <class ‘tuple’> (参数args的类型为tuple)

def myfunc(printtime=2, args2="default", **kwargs ):
     for r in range(printtime):
         print(f"printargs:{args2}{kwargs}")
myfunc(a=2,b=6,c=1,printtime=2)

tuple1 = (1,2,4,5)
def myfunc(a,b,c,d):
    print(a,b,c,d)
myfunc(*tuple1)  # 1 2 4 5
print(*tuple1)  # 1 2 4 5

dict1= {"a":1, "b":2, "c":3, "d":1}
myfunc(**dict1)  # 1 2 3 1

# 函数的嵌套调用
x=100
def funcO():
    x=0
    def funcA():
        x=1
        def funcB(): # 定义内部函数funcB
            nonlocal x
            x=2
            print(f'in funcB,x={x}')
        funcB()  # 在函数funcA内部调用funcB
        print(f'in funcA, x={x}')
    funcA()  # 调用函数funcA
    print(f'in funcO, x={x}')
funcO()
print(f'in global, x={x}')
# in funcB,x=2
# in funcA, x=2
# in funcO, x=0
# in global, x=100

# 函数的闭包初学概念
def funcA():
    x=100
    def funcB():
        print(x)
    return funcB
store_x = funcA()
store_x()  # 100
print('-'*100)
# 闭包实现存钱取钱案例
def atm_money(initial_money=0):
    def change(changemoney, mod=True):
        nonlocal initial_money
        if mod:
            initial_money+=changemoney
            print(f"+{changemoney}, 余额{initial_money}")
        else:
            initial_money-=changemoney
            print(f"-{changemoney}, 余额{initial_money}")
    return change
change = atm_money() # 将返回的change函数赋予给change变量
change(100) # 存100
change(10, False) # 取10
change(100)
# +100, 余额100
# -10, 余额90
# +100, 余额190
# 使用闭包定义连加函数
def initial_addfunc():
    '''
    闭包中的外层函数, 负责存储数据(小全局变量)并返回内层函数
    若将返回值赋予给一个全局变量对象, 此时内层函数=变量
    '''
    all_add = 0
    odd_add = 0
    even_add = 0
    def addfunc(x=0, y=0):
        """
        addfunc函数接收x和y两个int参数, 实现从x-y的连加和
        :param x:表示连加起点
        :param y:表示连加终点
        """
        nonlocal odd_add, even_add, all_add
        for active_num in range(x,y+1):
            all_add += active_num
            if active_num % 2 == 1:
                odd_add += active_num
            elif active_num % 2 == 0:
                even_add += active_num
            else:
                print('请输入大于零的整数!')
                break
        print(f'{x}-{y}连加和为{all_add}')
        print(f'奇数和为{odd_add}')
        print(f'偶数和为{even_add}')
    return addfunc
addfunc = initial_addfunc()
addfunc(1,10)
# 1-10连加和为55
# 奇数和为25
# 偶数和为30

def testfunc():
    pass

addB = lambda x, y : x + y  # 定义一个lambda匿名函数并赋予给变量addB
print(type(addB))  # addB变量的类型为<class 'function'>
print(addB(1,2))  # 3

# 函数递归计算阶乘
def facB(num):
    if num==1:
        return 1
    else:
        return num*facB(num-1)
print(facB(5))  # 120
print('-'*100)

# 计算斐波那契数列的第n项的值
def fac(n):
    if n == 1 or n == 2:
        return 1
    else:
        return (fac(n-1) + fac(n-2))  # 再次调用fac()将n-2传入
print(fac(9))  # 34
# 求斐波那契数列前n项和
def fac_sum(n):
    sum = 0
    for i in range(1,n+1):
        sum += fac(i) 
    return sum
print(fac_sum(5))  # 12
print('-'*100)

# 递归+闭包复习
# 计算阶乘前n项和
def calc_N(n):  # 计算阶乘函数
    if n == 1:
        return 1
    else:
        return n * calc_N(n-1)
    
def cal_closureA():  # 外层闭包func
    sum_calcA = 0
    def sum_calc_N(n):  # 内层求和func
        nonlocal sum_calcA
        for n in range(1, n + 1):
            sum_calcA += calc_N(n)
        return sum_calcA
    return sum_calc_N
calfuncA = cal_closureA()  # 将外层函数返回的内层函数sum_calc_N赋予给对象calfuncA
print(calfuncA(3))  # 9
print('-'*100)

# 迭代器和可迭代对象
listA = [1,2,3,4]  # 创建一个列表, 其是可迭代的iterable, 具有__iter__方法
# 使用内置函数iter(), 可得到一个可迭代的对象的迭代器对象[iterator]
iteratorA = iter(listA)  # 这个迭代器对象具有__next__方法
print(next(iteratorA))  # 1
print(next(iteratorA))  # 2
for i in iteratorA:
    print(i)

# 生成器
def functestA(n):
    while n > 0:
        yield n  # 
        n -= 1
    return  # 由于这是一个生成器函数, 这里的return等价于raise Stopiteration, 不写也没事

g = functestA(5)
print(next(g))  # 5
print(next(g))  # 4

for i in g:
    print(i)  # 3,2,1


