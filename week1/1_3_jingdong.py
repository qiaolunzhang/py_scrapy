import requests

url = "https://item.jd.com/12141397980.html"

try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
    print(r.url)
except:
    print("爬取失败")