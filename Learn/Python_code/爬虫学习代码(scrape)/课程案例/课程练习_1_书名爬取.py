# info
url = "https://books.toscrape.com/"
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
target_info = BS_outcome.find_all("p", attrs={"class":"price_color"})

# for i in target_info:
#      print(f"{i.string[2:]}")