import requests
import os





# 定义视频地址
video_url = "https://www.bilibili.com/video/BV114414Y7sQ"

# 发送请求并获取响应
response = requests.get(video_url)

# 获取视频标题
video_title = response.headers["Content-Disposition"].split("=")[1]

# 创建视频文件夹
if not os.path.exists("videos"):
    os.mkdir("videos")

# 保存视频文件
with open(f"videos/{video_title}", "wb") as f:
    f.write(response.content)

print("视频已下载")
