
import pprint, requests
# 
url = "https://dict.youdao.com"
print("网易有道翻译: https://dict.youdao.com\n退出查询: quit()\n------------------------------\n示例:\n请输入要查询的单词:insinuation\n'n. 暗示；暗讽；间接的讽刺'\n------------------------------")
while True:
    word = input("请输入要查询的单词:")
    if word == "" or word == " ":
        continue
    elif word != 'quit()':
        # 定义完整请求网址
        _url = f"/suggest?num=5&ver=3.0&doctype=json&cache=false&le=en&q={word}"
        complete_url = url+_url
        head = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
        }
        data = {
            'num': '5',
            'ver': '3.0',
            'doctype': 'json',
            'cache': 'false',
            'le': 'en',
            'q': 'cat'
        }  # 有道翻译的data直接传在网页网址上的(不知道为啥)

        request = requests.get(url=complete_url, headers=head)
        explain = request.json()["data"]["entries"][0]["explain"]
        print(explain)
    else:
        print("已退出翻译")
        break
