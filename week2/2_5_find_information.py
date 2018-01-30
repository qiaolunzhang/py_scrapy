import requests
from bs4 import BeautifulSoup
import re

r = requests.get('https://python123.io/ws/demo.html')
demo = r.text

soup = BeautifulSoup(demo, 'html.parser')

# 信息提取的方法
# 1. 形式解析：完整解析信息标记形式，再提取关键信息
# 2. 无视标记形式，直接搜索

# 可以综合两种方法来进行查找
# 1) 搜索到所有<a>标签
# 2) 解析<a>标签格式，提取href后的链接内容

for link in soup.find_all('a'):
    print(link.get('href'))

# .find_all(name, attrs, recursive, string, **kwargs)
# 返回一个列表类型，存储查找到的结果

# 查找对应标签类型
print(soup.find_all(['a', 'b']))
print(len(soup.find_all(['a', 'b'])))

for tag in soup.find_all(True):
    print(tag.name)

# 查找指定标签，指定属性值
print('*******************************************')
print(soup.find_all('p', 'course'))

# 极好，查找指定开头的标签
print('*******************************************')
print(soup.find_all(id=re.compile('link')))

print('*******************************************')
print(soup.find_all(string = 'Basic Python'))
print(soup.find_all(string = re.compile('python')))
