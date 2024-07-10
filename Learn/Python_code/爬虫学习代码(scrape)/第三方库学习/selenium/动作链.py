

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
start = time.time()

# 指定driver位置并设置浏览器参数
service = Service(executable_path="D:\Program File\python\python app\chromedriver-win64\chromedriver.exe")
opt = Options()
opt.debugger_address = '127.0.0.1:10000'
opt.add_argument('--disable-blink-features=AutomationControlled')  # 隐藏一些自动化痕迹
opt.add_experimental_option('excludeSwitches', ['enable-automation'])  # 隐藏自动执行的显示标识
# opt.add_experimental_option('detach', True)  # 禁止浏览器自动退出
opt.page_load_strategy = 'none'  # 设定加载策略
# 无头浏览器(可后台运行)
# opt.add_argument("--headless")
# opt.add_argument('--disable-gpu')
# opt.add_argument("--window-size=2000,1600") # 设置窗口大小

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
url = "https://www.12306.cn/"
google_url = "https://www.google.com/"
browser.get(url)
# time.sleep(2)
# 悬停在'车票'上, 并点击单程
element = browser.find_element(By.XPATH, '//*[@id="J-chepiao"]/a')
element2 = browser.find_element(By.XPATH, '//*[@id="megamenu-3"]/div[1]/ul/li[3]/a')
# 通过ActionChains()中的move_to_element()方法设置鼠标悬停
time.sleep(1)  # 隐式等待后检索到元素后等待1s等待图标加载出来(硬性)
ActionChains(browser)\
    .move_to_element(element)\
    .pause(.1)\
    .click(element2)\
    .perform()  

# 输入出发地
# time.sleep(1)
input1 = browser.find_element(By.XPATH, '//*[@id="fromStationText"]')
time.sleep(.1)
input1.click()
input1.send_keys('德安', Keys.ENTER)
# 输入目的地
# time.sleep(.1)
input2 = browser.find_element(By.XPATH, '//*[@id="toStationText"]')
input2.click()
input2.send_keys('杭州', Keys.ENTER)
# 修改出发日期
# time.sleep(.1)
input3 = browser.find_element(By.XPATH, '//*[@id="train_start_date"]')
input3.clear()
input3.send_keys('2024-02-11', Keys.ENTER)
# 点击学生票
# time.sleep(.1)
browser.find_element(By.XPATH, '//*[@id="toolbar_Div"]/div[2]').click()  # 点击空白
# time.sleep(.1)
browser.find_element(By.XPATH, '//*[@id="sf2"]').click()
# time.sleep(.1)
# 点击查询
browser.find_element(By.XPATH, '//*[@id="_a_search_btn"]').click()
# time.sleep(2)
# 勾选'按出发时间排序'
select1 = browser.find_element(By.XPATH, '//*[@id="sort_type"]')
time.sleep(.5)
Select(select1).select_by_visible_text('按出发时间排序')
end = time.time()
print(f'总耗时{end - start}s')

# browser.close()  # 关闭当前一个标签页
# browser.quit()  # 关闭整个浏览器