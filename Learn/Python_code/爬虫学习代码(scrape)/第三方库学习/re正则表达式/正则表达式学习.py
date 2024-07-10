# 导入re模块
import re
# 打开文本内容
with open(r"D:\Program File\My-Code\Learn\Python爬虫学习\test.txt", "r+", encoding="utf-8") as str:
    # 练习单字符匹配
    # str_data = str.read()
    # re_findall_result = re.findall(r"\d", str_data)  # 匹配所有0-9的数字
    # print(f"{re_findall_result}\ntype: {type(re_findall_result)}\n")
    # re_findall_result2 = re.findall(r"[A-Za-z0-9]", str_data)  # 匹配所有字母以及数字
    # print(f"{re_findall_result2}\ntype: {type(re_findall_result2)}\n")
    
    # 账号查找练习(匹配6-10位的字母加数字组合)
    # for str_data in str:
    #     if re.findall("^[0-9a-zA-Z]{6,10}$", str_data):
    #         print(re.findall("^[0-9a-zA-Z]{6,10}$", str_data))  
    # 匹配长度6-10, 纯数字且开头不为零的数字
    # for str_data_line in str:
    #     # print(str_data_line)
    #     if re.findall("^[1-9]{1}[0-9]{5,9}$", str_data_line):
    #         result = re.findall("^[1-9]{1}[0-9]{5,9}$", str_data_line)
    #         print(result)
    
    #  匹配邮箱
    for str_data_line in str:
        result = re.findall(r"(^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)*@(qq|gmail|outlook){1}(\.[a-zA-Z0-9]+)*$)", str_data_line)
        print(result)
