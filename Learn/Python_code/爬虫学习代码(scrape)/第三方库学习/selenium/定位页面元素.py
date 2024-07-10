

# 导入
from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # 指定driver位置
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By  # find策略
from selenium.webdriver.common.keys import Keys  # 传入数据
from selenium.webdriver.support.wait import WebDriverWait  # 显式等待
from selenium.webdriver.support import expected_conditions as executable_path
from selenium.webdriver.common.action_chains import ActionChains

# 指定driver位置并设置浏览器参数
service = Service(executable_path="D:\Program File\python\python app\chromedriver-win64\chromedriver.exe")
opt = Options()
opt.add_argument('--disable-blink-features=AutomationControlled')  # 隐藏一些自动化痕迹
opt.add_experimental_option('excludeSwitches', ['enable-automation'])  # 隐藏自动执行的显示标识
opt.add_experimental_option('detach', True)  # 禁止浏览器自动退出
opt.page_load_strategy = 'none'  # 设定加载策略

# 打开浏览器
browser = webdriver.Chrome(service=service, options=opt)
browser.implicitly_wait(5)  # 设定全局隐式等待
browser.maximize_window()  # 最大化窗口
# browser.set_window_size(1400,800)  # 设置窗口位置和大小
# browser.set_window_position(13,25)

# 网址
bilibili_url = "https://www.bilibili.com/"
google_url = "https://www.google.com/"
# 请求
start = time.time()
browser.get(bilibili_url)
end = time.time()
print(end - start)

# 通过explicit waits检查元素是否存在
# located = (By.XPATH, '//*[@id="i_cecream"]/div[2]/div[1]/div[3]/div[2]/div[1]/a[1]')
# wait = WebDriverWait(browser, timeout=2)
# wait.until(executable_path.presence_of_element_located(located))

# 通过By.XPATH检索'番剧'元素
anime_element = browser.find_element(By.XPATH, '//*[@id="i_cecream"]/div[2]/div[1]/div[3]/div[2]/div[1]/a[1]')
anime_url = anime_element.get_attribute('href')
print(f'番剧页面的链接是: {anime_url}')
anime_element.click()
time.sleep(2)
browser.switch_to.window(browser.window_handles[0])
time.sleep(1)
browser.refresh()
browser.switch_to.new_window('tab')
time.sleep(2)
browser.get(anime_url)

# # 输入数据并搜索
# search_element = browser.find_element(By.CLASS_NAME, "nav-search-input")
# search_element.send_keys("坐杀博徒",Keys.ENTER)

# browser.close()  # 关闭当前一个标签页
# browser.quit()  # 关闭整个浏览器