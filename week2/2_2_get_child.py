import requests
from bs4 import BeautifulSoup

# .content：子节点的列表
# .children：子节点的迭代类型
# .descendants: 子孙节点的迭代类型，包含所有子孙节点，用于循环遍历
r = requests.get('https://python123.io/ws/demo.html')
demo = r.text

soup = BeautifulSoup(demo, 'html.parser')
print(soup.head)
print(soup.head.contents)
print(soup.body.contents)
print(len(soup.body))