import requests

url = 'https://www.amazon.com/Amazon-Essentials-6-Pack-Crewneck-Undershirts/dp/B06XW85TSB/ref=lp_17567305011_1_1?s=apparel&ie=UTF8&qid=1516781349&sr=1-1&nodeID=17567305011&psd=1'
try:
    kv = {'user-agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text)
except:
    print('爬取失败')
