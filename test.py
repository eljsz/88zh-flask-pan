# -*- coding: utf-8 -*-

import re

def convert_links_to_html(text):
    # 定义链接的正则表达式模式
    link_pattern = re.compile(r'\[([^]]+)\]\((https?://\S+)\)', re.IGNORECASE)

    # 使用findall方法找到所有匹配的链接
    links = link_pattern.findall(text)

    # 如果存在链接，则将其替换为<a>标签
    if links:
        for original, link in links:
            # 使用正则表达式替换链接为<a>标签
            text = re.sub(re.escape(f'[{original}]({link})'), f'<a href="{link}">{original}</a>', text)

    return text

# 示例文本
sample_text = """
名称：**繁花(2023) 4K高码率+杜比视界+普沪双语多格式音轨 S01全**

简介：九十年代的上海处处是机遇与希望。青年阿宝凭借改革开放的春风和自己的打拼跻身成为商界后起之秀，黄河路上无人不晓。平凡阿宝蜕变为宝总，离不开高人爷叔与夜东京老板玲子、外贸大楼汪小姐的鼎力协助。随着神秘女子李李空降黄河路，一家时髦饭店即将搅动整条街，也令宝总原本决胜千里的事业变得动荡惊心，他与身边人的关系也经受着前所未有的考验。于此同时，深圳股市的过江龙强总也随时会给阿宝致命一击。阿宝唯有向前，以赤子之心翻越高山，方可奔赴繁花满眼。

标签：#繁花 #剧情
大小：119G

链接：
[https://www.alipan.com/s/dQuiEks27FW](https://www.alipan.com/s/dQuiEks27FW)


🔗：[ 其它频道与网站 ](https://t.me/Aliyun_4K_Movies/4058)
🌐：[群主都在用的机场，最低12￥/月](https://lcloud.wiki/#/register?code=wYZUygaP)
"""

# 将链接转换为HTML的<a>标签
converted_text = convert_links_to_html(sample_text)

# 打印结果
print(converted_text)
