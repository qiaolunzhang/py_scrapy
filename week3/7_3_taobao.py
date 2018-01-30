import requests
import re


def get_html_text(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return " "


def parse_page(ilt, html):
    print("")


def print_good_list(ilt):
    print("")


def main():
    goods = "书包"
    depth = 2
    start_url = 'https://s.taobao.com/search?q=' + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44*i)
            html = get_html_text(url)
            parse_page(infoList, html)
        except:
            continue
    print_good_list(infoList)
