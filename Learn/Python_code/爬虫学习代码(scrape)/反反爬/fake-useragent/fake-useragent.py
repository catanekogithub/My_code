from fake_useragent import UserAgent
import requests
import time

# 创建一个UserAgent库对象
ua = UserAgent()
# 使用UserAgent中的random方法随机赋予一个ua给变量
useragent = ua.random
# 将随机获取到的ua写入请求头
headers = {'User_Agent':useragent}
# 请求网址
url = 'https://www.baidu.com'
request = requests.get(url=url, headers=headers)
print(request)