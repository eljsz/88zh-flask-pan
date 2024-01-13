# -*- coding: utf-8 -*-
# @Time    : 2024/1/6
# @Author  : lhq
# @File    : yunpan1.py
# @Description :
import requests
from lxml import etree

def yunpan1(keyword):
    headers = {
        'authority': 'yunpan1.cc',
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
        'accept-language': 'zh-CN,zh;q=0.9',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'flarum_session=Lr0k4Vo6fcpHlW3KBAVFwH6rX281mCOSjMYQnJ41; __vtins__JeZdgfqHgYyGlHfa=%7B%22sid%22%3A%20%227759f52d-b907-5b07-b3ea-494131c5f327%22%2C%20%22vd%22%3A%201%2C%20%22stt%22%3A%200%2C%20%22dr%22%3A%200%2C%20%22expires%22%3A%201704556152487%2C%20%22ct%22%3A%201704554352487%7D; __51uvsct__JeZdgfqHgYyGlHfa=1; __51vcke__JeZdgfqHgYyGlHfa=023d8388-51ce-5e9a-b0be-86577607f5ea; __51vuft__JeZdgfqHgYyGlHfa=1704554352493; __51huid__JrKC8MsOnjkWL5ep=03a86d7c-1c91-55d0-bc98-64a25f8a77cb',
    }

    params = {
        'q': keyword,
    }

    response = requests.get('https://yunpan1.cc/', params=params, headers=headers).text
    html = etree.HTML(response)

    titles = html.xpath('//*[@id="flarum-content"]/div/ul/li/a/text()')
    title = [s.replace('\n', '').strip() for s in titles]

    urls = html.xpath('//*[@id="flarum-content"]/div/ul/li/a/@href')

    result = [{"title": title, "url": url} for title, url in zip(title, urls)]
    return result