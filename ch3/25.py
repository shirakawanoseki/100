
""" 言語処理100本ノック 2015 第3章: 正規表現
25. テンプレートの抽出
記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．
"""

import sys
import json
import gzip
import re

with gzip.open(sys.argv[1], "rt") as f:
    template = {}
    for data_line in f:
        js = json.loads(data_line)
        if js["title"] == 'イギリス':
            #基礎情報のセクションを先読
            basic_info = re.search(r'^\{\{基礎情報 国(.+?)\}\}$', js["text"], flags = (re.MULTILINE | re.DOTALL))
            #改行文字で分割
            splitted_basic_info = basic_info.group(0).split('\n')
            #分割した各行の内、パターンにマッチするものを辞書オブジェクトに格納
            for basic_info_line in splitted_basic_info:
                match_result = re.match(r'\|(.*?)\s+=\s+(.*)', basic_info_line)
                if match_result:
                    template[match_result.group(1)] = match_result.group(2)

    print(template)

