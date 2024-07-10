import requests, os, re

# 定义信息
# url = "https://www.jdlingyu.com/tuji?post_order=views"
url = "https://www.jdlingyu.com/tuji?post_order=views"
url_public_str = "https://img.jdlingyu.com/"
head = {
     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
}
proxy = {"https":"127.0.0.1:10809"}

# 获取主要str格式网页源码
main_web_html_str = requests.get(url=url, headers=head, proxies=proxy).text

# 首页匹配数据
# 每个列表页的链接: <a  target="_blank" href="https://www.jdlingyu.com/59062.html" rel="nofollow" class="thumb-link"><picture class="picture" ><source type="image/webp" srcset="https://img.jdlingyu.com/images/2021/09/06/7.jpg" /><img  class="post-thumb lazy" data-src="https://img.jdlingyu.com/images/2021/09/06/7.jpg"   alt="萌白酱（甜味弥漫） &#8211; 骚断腿系列" src="https://img.jdlingyu.com/images/2021/09/06/7.jpg"/></picture></a>
# 正则: <a  target="_blank" href="(.*?)" rel="nofollow" class="thumb-link"><picture class="picture" ><source type="image/webp" srcset=".*?" /><img  class="post-thumb lazy" data-src=".*?"   alt="萌白酱（甜味弥漫） &#8211; 骚断腿系列" src=".*?"/></picture></a>
# 提取主页数据
list_page_url_list = re.findall(r'<a  target="_blank" href="(.*?)" rel="nofollow" class="thumb-link"><picture class="picture" ><source type="image/webp" srcset=".*?" /><img  class="post-thumb lazy" data-src=".*?"   alt="(.*?)" src=".*?"/></picture></a>', main_web_html_str)
# print(list_page_url_list)
# print(type(list_page_url_list))
# 处理获取到的列表页地址和文件夹名称
for list_page_url_and_name in list_page_url_list:
    list_page_url_and_name_str = str(list_page_url_and_name)  # 将元组类型转换为字符串
    print(type(list_page_url_and_name_str))
    print(list_page_url_and_name_str)
    folder_name = list_page_url_and_name_str.split(",")[-1][2:-2]
    print(folder_name)
    list_page_url = list_page_url_and_name_str.split(",")[0][2:-1]
    print(list_page_url)

    # 请求列表页(详情页)源码
    list_page_html_str = requests.get(url=list_page_url, headers=head, proxies=proxy).text

    # 详情页匹配数据
    # 多张单页的每张图片地址: <img src="https://img.jdlingyu.com/images/2021/09/06/7.jpg" alt="(7)" border="0">
    # 单张翻页的每张图片地址
    