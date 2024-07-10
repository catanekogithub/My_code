
# 导入
import requests
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

# selenium部分
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
# browser.maximize_window()  # 最大化窗口
# browser.set_window_size(1400,800)  # 设置窗口位置和大小
# browser.set_window_position(13,25)

# 运行stealth.min.js反检测
with open("D:\Program File\python\python app\chromedriver-win64\stealth.min.js") as f:
    js = f.read()
browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": js
})

# 网址
url = 'https://www.gamewallpapers.com/'
url2 = 'https://bilibili.com/'

browser.get(url)
print(browser.title)
# print(browser.page_source)
# browser.switch_to.new_window('tab')
# response = browser.get(url)
# time.sleep(2)

a = 1
# print(type(browser.find_element(By.XPATH, f'//*[@id="thumbnails-left-content"]/div[{a}]')))
for x in browser.find_elements(By.XPATH, f'//div[@id="thumbnails-left-content"]'):
    # print(browser.find_elements(By.XPATH, f'//div[@id="thumbnails-left-content"]'))
    time.sleep(1)
    i = x.find_element(By.XPATH, '//*[@id="thumbnails-left-bar"]//h1[@class]/a[last()]')
    print(i.text)
    # x = f.get_attribute('href')
    # print(x)
    # print()
    a += 1
    # for i in thumbnails_left_content_all:
        # f = i.find_element(By.XPATH, '/div[@id="thumbnails-left-bar"]/h1/a[last()]')
        # print(f)
    # print(thumbnails_left_content_all)
    # browser.refresh()
    time.sleep(1)

    # break
    


    # thumbnails_left_bar_click_el.send_keys(Keys.ENTER)
    # href = thumbnails_left_bar_click_el.get_attribute('href')
    # print(href)

    # # browser.switch_to.new_window('tab')
    # # browser.get(href)
    # time.sleep(1)
    # # browser.switch_to.window(browser.window_handles[-1])
    # # href = browser.find_element(By.XPATH, '//*[@id="thumbnails-left-content"]/a[2]').get_attribute('href')
    # browser.find_element(By.XPATH, '//*[@id="thumbnails-left-content"]/a[2]').send_keys(Keys.ENTER)
    # src = browser.find_element(By.XPATH, '/html/body/center/img').get_attribute('src')
    # browser.get(src)
    # time.sleep(1)
    # browser.back()
    # browser.back()
    # browser.back()
    # # browser.switch_to.window(browser.window_handles[0])
    # time.sleep(1)
    # browser.close()
    # el.click
    # browser.get(href)






# requests请求以及写入部分
# # info
# headers = {
#      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
# }  # 加完UA能请求到就不用再加其他的(cookie, host等)
# proxy = {"https":"127.0.0.1:10809"} 

# url = "https://pixiv.canaria.cc/img-master/img/2024/01/24/00/59/43/115429069_p0_master1200.jpg"
# # url_public = "https://wallroom.io"
# response = requests.get(url=url, headers = headers, proxies= proxy)
# # ----------------------------------------------------
# if response.ok == True:
#     print(f'请求成功\n状态码:{response.status_code}')
# else:
#      print("请求失败")
#      print(f'状态码:{response}')
# #  ---------------------------------------------------
# url_content = response
# with open(r"D:\Program File\My-Code\Learn\python scrape study code\爬取资源存放\temp\\" + "114514"+ ".jpg", 'wb') as f:
#      # 使用requests模块的.content方法提取二进制数据, "wb", w-write, b-binary(二进制)
#      f.write(url_content.content)
