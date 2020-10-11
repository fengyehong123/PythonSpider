import requests

url = "https://www.baidu.com/"

# 准备浏览器的头部信息
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/80.0.3987.163 Safari/537.36"
}

# 发送请求,获取响应
response = requests.get(url, headers=headers)

# 获取网页信息
html = response.content.decode("utf-8")

# 把网页信息保存到本地,需要指定编码方式,否则会报错
with open("百度.html", "w", encoding="utf-8") as file:
    file.write(html)
