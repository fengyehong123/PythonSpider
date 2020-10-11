import requests

url = "https://www.baidu.com/s"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/80.0.3987.163 Safari/537.36"
}

# 准备参数
params = {
    "wd": "python",
    "a": "c"
}

# 发送请求,获取响应
response = requests.get(url, headers=headers, params=params)

# 提取数据
html = response.content.decode("utf-8")

with open("百度1.html", "w", encoding="utf-8") as file:
    file.write(html)
