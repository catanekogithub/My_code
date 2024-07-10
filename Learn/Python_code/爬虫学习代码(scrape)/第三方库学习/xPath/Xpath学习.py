
# import requests

# url = "https://m.douban.com/rexxar/api/v2/movie/recommend"
# head = {
# 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
# }
# proxy = {"https":"127.0.0.1:10809"}
# parameters = {
#     'refresh': '0',
#     'start': '0',
#     'count': '20',
#     'selected_categories': '\{\}',
#     'uncollect': 'false',
#     'sort': 'T',
#     'tags': None
# }

# response = requests.get(url=url, headers=head, params=parameters)
# print(response)

import lxml