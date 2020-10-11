import requests

# 准备URL
url = "https://www.baidu.com/"

# 发送请求获取响应
response = requests.get(url)

"""
response对象中常见的属性
"""

# 响应体 str类型
print(response.text)
# 响应体 bytes类型
print(response.content)
# 响应头
print(response.headers)
# 响应对应的请求头
print(response.request.headers)
# 响应对应的cookie
print(response.cookies)
# 响应状态码
print(response.status_code)




