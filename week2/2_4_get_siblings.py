import requests
from bs4 import BeautifulSoup

# next_sibling
# next_siblings
# previous_sibling 迭代类型，用于for in中
# previous_siblings
r = requests.get('https://python123.io/ws/demo.html')
demo = r.text

soup = BeautifulSoup(demo, 'html.parser')

print(soup.a.parent)
print('*******************************************')
print(soup.a.next_sibling)
print(soup.a.previous_sibling)
