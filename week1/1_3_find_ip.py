import requests

url = 'http://www.ip138.com/ips138.asp'
try:
    kv = {'ip':'8.8.8.8'}
    r = requests.get(url, params=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[-500])
    print(r.request.url)
except:
    print('爬取失败')
