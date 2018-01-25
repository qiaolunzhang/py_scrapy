import requests

try:
    kv = {'wd':'生活'}
    agent = {'user-agent': 'Mozilla/5.0'}
    r = requests.get(url='http://www.baidu.com/s', params=kv, headers=agent)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text)
    print(r.request.url)
except:
    print('爬取失败')