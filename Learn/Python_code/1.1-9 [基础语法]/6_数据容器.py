
# list (列表)

# 从[1, 2, 3, 4, 5, 6, 7, 8, 9]列表中取出偶数并组成新的列表list_new
# while循环
list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 定义空列表
list_new = []
i = 0
while i < len(list_num):
    check = int(list_num[i])
    if check % 2 == 0:
        list_new.append(check)
    i += 1
print(list_new)
# for-in循环
list_new = []
for check_2 in list_num:
    if check_2 % 2 == 0:
        list_new.append(check_2)
print(list_new)


# dict数据容器升职加薪练习
staff_condition = {"王力宏": {"部门": "科技部", "工资": 3000, "级别": 1}, "周杰伦": {"部门": "市场部", "工资": 5000, "级别": 2}, "林俊杰": {"部门": "市场部", "工资": 7000, "级别": 3}}
print(f"原始员工信息为:{staff_condition}")
for key_staffname in staff_condition:
        if staff_condition[key_staffname]["级别"] == 1:
            staff_condition[key_staffname]["级别"] += 1
            staff_condition[key_staffname]["工资"] += 1000
print(f"加薪后的员工信息为{staff_condition}\n\n")

# 使用split()语句将str处理成list
txt = "hello, my name is Peter, I am 26 years old"
x = txt.split(", ")
print(f'{x}的类型是{type(x)}')       

print('')
print('')
print('')

# list中的内置方法index()的使用
list1=[1,3,4,3,45,77]              

print(list1.index(77))

# str中的内置方法split()
txt = "hello, my name is Peter, I am 26 years old"
x = txt.split(", ")
print(x)
print(f'{x}的类型是{type(x)}')

print(4 and 6+1 and 4+1>10)
print((not 1) or (not 2+1) or (not 4+1))
