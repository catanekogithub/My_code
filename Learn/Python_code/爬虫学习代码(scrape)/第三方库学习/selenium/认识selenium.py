

# 导入
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
# 实例化浏览器
service = Service(executable_path="D:\Program File\python\python app\chromedriver-win64\chromedriver.exe")
opt = Options()
opt.add_argument('--disable-blink-features=AutomationControlled')
browser = webdriver.Chrome(service=service, options=opt)
browser.maximize_window()  # 最大化窗口
# browser.set_window_size(1400,800)  # 设置窗口位置和大小
# browser.set_window_position(13,25)

# 网址
url = "https://www.bilibili.com/"
url1 = "https://www.google.com/"
# 请求


browser.get(url)
time.sleep(2)
browser.get(url1)
browser.back()  # 回退
time.sleep(2)
browser.forward()  # 向前
time.sleep(2)
browser.refresh
time.sleep(2)
page_text = browser.page_source
print(page_text)



browser.close()  # 关闭当前一个标签页
# browser.quit()  # 关闭整个浏览器