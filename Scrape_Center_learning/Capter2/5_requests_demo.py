import requests
import re
from requests.auth import HTTPBasicAuth

from sympy import false

# r = requests.get('https://ssr1.scrape.center/')
# print(r.text)

# r = requests.get('http://httpbin.org/get')
# print(r.status_code)
# print(r.text)

# data = {
#     'name': 'chenangang',
#     'age': 19
# }
# r = requests.get('http://httpbin.org/get',params=data)
# print(r.text)

# r = requests.get('http://httpbin.org/get')
# print(type(r.text))
# print(r.json())
# print(type(r.json()))

# 抓取网页，只要电影名称
# r = requests.get('https://ssr1.scrape.center/')
# pattern = re.compile('<h2.*?>(.*?)</h2>', re.S)
# titles = re.findall(pattern, r.text)
# print(titles)
# print(type(titles))

# # 抓取百度的小图标
# r = requests.get("https://www.baidu.com/favicon.ico")
# # wb ,以二进制的形式写入文件
# with open('favicon.ico', 'wb') as f:
#     f.write(r.content)

# data = {
#     'userAccount': 'chenangang',
#     'password': 12345678
# }
# r = requests.post('http://httpbin.org/post',data=data)
# print(r.text)

# r = requests.get('https://ssr1.scrape.center/')
# print(type(r.status_code), r.status_code)
# print(type(r.cookies), r.cookies)
# print(type(r.headers), r.headers)
# print(type(r.url), r.url)
# print(type(r.history), r.history)

# r = requests.get('https://ssr1.scrape.center/')
# exit() if not r.status_code == requests.codes.ok else print('Request successfully')

# 文件上传
# files = {'file': open('favicon.ico', 'rb')}
# r = requests.post('http://httpbin.org/post', files=files)
# print(r.text)

# 获取cookie
# r = requests.get('https://www.baidu.com')
# print(r.cookies)
# for key,value in r.cookies.items():
#     print(key + '=' + value)

# 通过设置cookies来模拟github的登陆
# headers = {
#     'Cookie': '_octo=GH1.1.1506817113.1755857168; _device_id=611eac3ab89272f71a07a47bd7c74e8a; saved_user_sessions=84366210%3AffTqNyM2TZs4F3QdQRjJy1F9eD6nG43rrahp_KEHGQiOWzgR; user_session=ffTqNyM2TZs4F3QdQRjJy1F9eD6nG43rrahp_KEHGQiOWzgR; __Host-user_session_same_site=ffTqNyM2TZs4F3QdQRjJy1F9eD6nG43rrahp_KEHGQiOWzgR; logged_in=yes; dotcom_user=cyb-best; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; cpu_bucket=xlg; preferred_color_mode=dark; tz=Asia%2FShanghai; _gh_sess=dEnV3pr5yy3AT0HFnUVmGrfPk%2BsByaKhc6B%2B2UVUlfGJ%2B%2FNWXnHB9VTUI9SZjbINCOqI2nAmiA4zpVeUYh9qbmsh48BSgbAQ0D4psh4nTvrLp4OQKQah4Eek8R%2FnixabIQX28TBEwfJr4Q5te35p9F6AQmG%2B3sW%2Bp5mjp1wh5%2FagX3LfOcbugeB2H6aIBzG372tmCe1hUqJGJehM7JejE7EAXfDNY3VxOdM5zWCot7Oyt%2BIVfO09Bj8JROUZLrlMfFKCPXSykWLUpTqCYL8njBUN2YuKlF5fpxPLWyhJwtfdOaihHBrCe5GN64QmUXDYuBr%2BYSKFbObXOEr1y2B5xh%2BeRlf1nrYyQtnlhVKTi4uIVYMTUAqS3Ug7yyeMywJa--jnep6tWI9qoSKJkb--JvpB943Zt4trEU3x%2F7o3yQ%3D%3D',
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36'
# }
# r = requests.get('https://www.github.com',headers=headers)
# print(r.text)
# print(r.cookies)
# print(r.status_code)

# session维持
# s = requests.session()
# s.get('http://httpbin.org/cookies/set/number/123456789')
# r = s.get('http://httpbin.org/cookies')
# print(r.text)

# # ssl证书验证
# r = requests.get('http://ssr2.scrape.center/',verify=false)
# print(r.text)

# 身份认证
# r = requests.get('https://ssr3.scrape.center/', auth=HTTPBasicAuth('admin', 'admin'))
# 可简写如下
r = requests.get('https://ssr3.scrape.center/', auth=('admin', 'admin'))
print(r.status_code)