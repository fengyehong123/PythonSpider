# coding:utf-8

import requests

# 1.url(url_list)
url = "https://www.baidu.com/"
# 添加headers
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}
# 2.发送请求,获取响应
response = requests.get(url, headers=headers)
# 3.提取数据
html = response.content.decode()

# 4.保存入库
with open("baidu.html", "w") as f:
    f.write(html)
