from urllib.request import urlopen
from urllib.error import HTTPError

try:
    html = urlopen("https://zhangqiaolun.com")
except HTTPError as e:
    #print(e)
    print("There is an error")
else:
    print('ok')