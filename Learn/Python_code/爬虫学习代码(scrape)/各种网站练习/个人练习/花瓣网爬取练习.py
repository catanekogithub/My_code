
# https://gd-hbimg.huaban.com/83c57dd518c76894b63e359905982959ecb0592174841-qvVBEk_fw658webp

# from selenium import webdriver
# url = 'https://huaban.com/search?q=cos'
# driver = webdriver.Chrome() #使用谷歌浏览器打开
# driver.maximize_window()  #放大全屏，可有可无
# driver.get(url) 
# data = driver.page_source #拿到代码放在data变量中
# with open('./test.html','w',encoding='utf-8') as fp:
#     fp.write(data) #存储在test.html中

import re
from bs4 import BeautifulSoup


with open(r'D:\Program File\My-Code\Learn\Python爬虫学习\huabanwebbody.html','r',encoding='utf-8') as html:
    # BS_result = BeautifulSoup(html, "html.parser")
    # bbc = BS_result.find_all("a", attrs={"class":"KGdb7ifV"})
    # list = []
    # for x in bbc:
    #     aac = bbc.find_all("img", attrs={"src":".*?"})
    #     list.append(aac.string)
    #     print(list)

    for bbc in html:
        print(type(bbc))
        target_info = re.findall(r'<img class="transparent-img-bg hb-image" (alt=".*?")* (title=".*?")* (src=".*?") srcset=".*?"', bbc)
        if target_info:
            for b in target_info:
                if b:
                    # a = b.split(" ")
                    # ','.join(a)
                    # print(type(a))
                    print(re.findall('src="(.*?)"', b))    
                # ','.join(b)
                # aac = re.findall(r'<a class="KGdb7ifV" href="(.*?)" target="_blank" rel="noreferrer">', b)
                # print(aac)


 