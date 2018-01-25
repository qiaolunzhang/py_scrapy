import requests

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"

if __name__ == "__main__":
    url = "http://www.tmall.com"
    print(getHTMLText(url))

    r = requests.head('http://httpbin.org/get')
    print(r.headers)
    print('*************************************')
    # 可以发现为空
    print(r.text)