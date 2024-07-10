# info
url = "https://wallroom.io/new"
url_public = "https://wallroom.io"
headers = {
     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
}  # 加完UA能请求到就不用再加其他的(cookie, host等)
proxy = {"https":"127.0.0.1:10809"} 
# proxy = {"https":"127.0.0.1:10000"} 


import requests
print(f"正在发送请求到 {url}")
response = requests.get(url=url, headers = headers, proxies=proxy)
# ----------------------------------------------------
if response.ok == True:
    print(f'请求成功\n状态码:{response.status_code}')
else:
     print("请求失败")
     print(f'状态码:{response}')
#  ---------------------------------------------------
html_str = response.text 

# from bs4 import BeautifulSoup
# BS_result = BeautifulSoup(html_str, "html.parser")


# 创建文件夹
# import os_一个用来创建文件夹的模块
# import os
# 使用os模块创建一个文件夹
# dir_name = "爬取资源"
# if not os.path.exists(dir_name):
#      os.mkdir(dir_name)

import time
# for target_url in target_urls_list:
#      time.sleep(0.3)
#      response = requests.get(url=target_url, headers= headers, proxies= proxy)
#      pic_name = target_url.split("/")[-1]
#      with open("D:\Program File\My-Code\Learn\Python爬虫学习\爬取资源\\" + "\\" + pic_name, 'wb') as f:
#           f.write(response.content)

# import re
# target_adress_list = re.findall(r"<div><a href='(.*?)'>", html_str)
# # 使用n变量记录第多少张
# n = 1
# for address in target_adress_list:
#      time.sleep(0.5)
#      # 原图完整下载地址参考: https://wallroom.io/img/3840x2160/bg-ef7c6b4.jpg
#      urls_complet = url_public + "/img" + address + ".jpg"  # 构建完整地址
#      # ////////////////////////
#      print(f"请求第{n}张图片中")
#      # ////////////////////////
#      response_fina_address = requests.get(url=urls_complet, headers= headers, proxies= proxy)
#      if response_fina_address.ok == False:  # 判断请求能否得到正常结果
#           # 重新构建完整地址
#           urls_complet = url_public + "/img" + address + ".png"
#           # 再次请求重构后的地址
#           response_fina_address = requests.get(url=urls_complet, headers= headers, proxies= proxy)
#      # 写入文件
#      pic_name = urls_complet.split("/")[-1]
#      with open(r"D:\Program File\My-Code\Learn\Python爬虫学习\爬取资源\wallroom.io\\" + pic_name, 'wb') as f:
#           # 使用requests模块的.content方法提取二进制数据, "wb", w-write, b-binary(二进制)
#           f.write(response_fina_address.content)

#      print(f"{urls_complet}\n写入完成")
#      n += 1
# print(f"爬取完成, 共爬取了{n}张图片")
