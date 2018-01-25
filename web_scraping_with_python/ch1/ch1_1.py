import requests
from urllib.request import urlopen
html = urlopen('http://pythonscraping.com/pages/page1.html')
print(html.read())

r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
print(r.status_code)

print(r.headers['content-type'], r.encoding)
print(r.text)
print(r.json())
