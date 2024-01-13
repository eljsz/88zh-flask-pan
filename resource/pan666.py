# -*- coding: utf-8 -*-
# @Time    : 2024/1/9
# @Author  : lhq
# @File    : pan666.py
# @Description :
from lxml import etree



def pan666(keyword):
    import requests

    headers = {
        'authority': 'pan666.net',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.139 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://pan666.cn/',
        'accept-language': 'zh-CN,zh;q=0.9',
    }

    params = {
        'q': keyword,
    }

    response = requests.get('https://pan666.net/', params=params, headers=headers).text

    html = etree.HTML(response)
    titles = html.xpath('//*[@id="flarum-content"]/div/ul/li/a/text()')
    title = [s.replace('\n', '').strip() for s in titles]

    urls = html.xpath('//*[@id="flarum-content"]/div/ul/li/a/@href')

    result = [{"title": title, "url": 'https://pan666.net/'+url} for title, url in zip(title, urls)]
    return result

