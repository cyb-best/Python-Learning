from pyquery import PyQuery as pq
# 通过Url初始化
doc = pq(url='https://cuiqingcai.com')
# print(doc)
print(doc('title'))