
# 导入
from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # 指定driver位置
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By  # find策略
from selenium.webdriver.common.keys import Keys  # 传入数据
from selenium.webdriver.support.wait import WebDriverWait  # 显式等待模块
from selenium.webdriver.support import expected_conditions as executable_path
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


# 指定driver位置并设置浏览器参数
service = Service(executable_path="D:\Program File\python\python app\chromedriver-win64\chromedriver.exe")
opt = Options()
opt.add_argument('--disable-blink-features=AutomationControlled')  # 隐藏一些自动化痕迹
# 通过selenium连接上独立配置的chrome浏览器
opt.debugger_address = '127.0.0.1:10000'
# opt.add_experimental_option('excludeSwitches', ['enable-automation'])  # 隐藏自动执行的显示标识
# opt.add_experimental_option('detach', True)  # 禁止浏览器自动退出
opt.page_load_strategy = 'none'  # 设定加载策略

# 打开浏览器
browser = webdriver.Chrome(service=service, options=opt)
browser.implicitly_wait(5)  # 设定全局隐式等待
browser.maximize_window()  # 最大化窗口
# browser.set_window_size(1400,800)  # 设置窗口位置和大小
# browser.set_window_position(13,25)

with open("D:\Program File\python\python app\chromedriver-win64\stealth.min.js") as f:
    js = f.read()
browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": js
})

# 网址
url = 'https://bot.sannysoft.com/'
url2 = 'https://bilibili.com/'

browser.get(url2)
print(browser.title)
# print(browser.page_source)
browser.switch_to.new_window('tab')
response = browser.get(url)
time.sleep(2)
browser.get(url2)
# time.sleep(1)
# print(browser.title)
# if browser.title == 'Antibot':
#     browser.switch_to.window(browser.window_handles[0])


# browser.close()  # 关闭当前一个标签页
# browser.quit()  # 关闭整个浏览器



