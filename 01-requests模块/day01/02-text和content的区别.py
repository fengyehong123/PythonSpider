import requests

url = "https://www.baidu.com/"

# 发送请求获取响应
response = requests.get(url)

# 关于text转换方式
response.encoding = "utf-8"
print(response.text)

"""
一般来说更加推荐使用 response.content.decode()的方式获取响应的html页面
"""
# 关于content转换方式
print(response.content.decode("utf-8"))

