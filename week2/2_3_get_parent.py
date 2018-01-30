import requests
from bs4 import BeautifulSoup

# .parent 节点的父亲标签
# .parents 节点的父辈标签的迭代类型，用于循环遍历先辈节点
r = requests.get('https://python123.io/ws/demo.html')
demo = r.text

soup = BeautifulSoup(demo, 'html.parser')

print(soup.title.parent)
print('***************************************')
print(soup.html.parent)
print('***************************************')
print(soup.parent)

# 遍历a标签的所有先辈
print('***************************************')
for parent in soup.a.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)