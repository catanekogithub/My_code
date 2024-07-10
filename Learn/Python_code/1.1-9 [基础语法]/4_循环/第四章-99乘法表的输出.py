"""while循环输出99乘法表
h = 1
while h <= 9:
    p = 1
    while p <= h:
        print(f"{p}*{h}={p*h}\t",end='')
        p += 1
    h += 1
    print()
"""
# for循环输出99乘法表
for n in range(1,10):
    for j in range(1,n+1):
        print(f"{j}*{n}={n*j}\t",end='')
    print()

