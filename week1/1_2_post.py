import requests

payload = {'wd': '生活'}
r = requests.post('https://www.baidu.com/s', params=payload)
r.encoding = r.apparent_encoding

print(r.text)


payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post('http://httpbin.org/post', data=payload)
print(r.text)
