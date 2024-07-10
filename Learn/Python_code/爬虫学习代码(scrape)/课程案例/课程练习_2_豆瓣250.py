# info
url = "https://movie.douban.com/chart"
headers = {
     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}  # 加完UA能请求到就不用再加其他的(cookie, host等)
# proxy = {"https":"127.0.0.1:10809"} 

import requests
response = requests.get(url=url, headers = headers)
# ------------------------------------------------------------
if response.ok == True:
    print(f'请求成功\n状态码:{response.status_code}')
else:
     print("请求失败")
     print(f'状态码:{response}')
#  -----------------------------------------------------------
html_str = response.text
# html_str存储的就是网页源码
# print(html_str)

from bs4 import BeautifulSoup
BS_outcome = BeautifulSoup(html_str, "html.parser")
# print(type(BS_outcome))
# 通过find_all(标签)定位并获取副标题大概内容
target_info = BS_outcome.find_all("div", attrs={"class":"pl2"})
# print(target_info_1)
# find_all会返回一个可迭代对象, 可使用for_in循环接收
list_name = []
for target_info_1 in target_info:
     all_main_title = target_info_1.find("a")
     for main_title in all_main_title:
          # print(main_title)
          if "/" in main_title:
               # 使用字符串的切片操作{序列[起始下标: 结束下标]}
               a = main_title.string[25:-27]
               print(f"{a}")
               list_name.append(a)
               # print(f"{type(main_title.string[25:])}")
i = list_name
print(f"{i}的类型是{type(i)}")

# 写进文件
f = open("D:\\Program File\\My-Code\\Learn\\Python爬虫学习\\test.txt", "w", encoding="utf-8")
n = 1
for x in i:
     f.write(f"{n}.{x}\n")
     n += 1
f.close()
