

# info
url = "https://pixiv.canaria.cc/img-master/img/2024/01/24/00/59/43/115429069_p0_master1200.jpg"
url_public = "https://wallroom.io"
headers = {
     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
}  # 加完UA能请求到就不用再加其他的(cookie, host等)
proxy = {"https":"127.0.0.1:10809"} 

response = requests.get(url=url, headers = headers, proxies= proxy)
# ----------------------------------------------------
if response.ok == True:
    print(f'请求成功\n状态码:{response.status_code}')
else:
     print("请求失败")
     print(f'状态码:{response}')
#  ---------------------------------------------------
url_content = response
with open(r"D:\Program File\My-Code\Learn\python scrape study code\爬取资源存放\temp\\" + "114514"+ ".jpg", 'wb') as f:
     # 使用requests模块的.content方法提取二进制数据, "wb", w-write, b-binary(二进制)
     f.write(url_content.content)



