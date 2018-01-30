import requests
from bs4 import BeautifulSoup

r = requests.get("https://python123.io/ws/demo.html")
demo = r.text

soup = BeautifulSoup(demo, 'html.parser')
print(soup.prettify())

tag = soup.a
print(tag)
print(tag.name)

print(soup.a.parent)

print('*************************************')
print(tag.attrs)
print(dir(tag))
print(type(tag))
print(type(tag.attrs))

print('*************************************')
print(soup.a)
print(soup.a.string)

print(soup.p)
print(soup.p.string)
print(type(soup.p.string))

print('************************************')
# 可以在下面看出，如果是用注释的话，会把注释的<!-- -->去掉
newsoup = BeautifulSoup("<b><!--This is a comment--></b><p>This is not a comment</p>", "html.parser")
print(type(newsoup.b.string))
print(newsoup.b.string)
print(type(newsoup.p.string))
print(newsoup.p.string)
