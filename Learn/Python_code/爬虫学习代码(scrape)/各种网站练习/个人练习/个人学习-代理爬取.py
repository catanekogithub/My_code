
url = "https://twitter.com/Barret_China"
headers = {
     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
}  # 加完UA能请求到就不用再加其他的(cookie, host等)
proxy = {"https":"127.0.0.1:10809"} 

import requests
response = requests.get(url=url, headers = headers, proxies=proxy)
# ----------------------------------------------------
if response.ok == True:
    print(f'请求成功\n状态码:{response.status_code}')
else:
     print("请求失败")
     print(f'状态码:{response}')
#  ---------------------------------------------------
response.encoding = response.apparent_encoding
print(response.text)
html_str = response.text

# from bs4 import BeautifulSoup
# BeautifulSoup_outcome = BeautifulSoup(html_str, "html.parser")
# print(f'BeautifulSoup(html_str, "html.parser")的类型为:{type(BeautifulSoup_outcome)}')




