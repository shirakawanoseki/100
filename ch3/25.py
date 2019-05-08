
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
            basic_info_iter = re.finditer(r'^\{\{基礎情報 国(.+?)\}\}$', js["text"], flags = (re.MULTILINE | re.DOTALL))
            for basic_info in basic_info_iter:
                splitted_basic_info = basic_info.group(0).split('\n')
                for basic_info_line in splitted_basic_info:
                    match_result = re.match(r'\|(.*?)\s+=\s+(.*)', basic_info_line)
                    if match_result:
                        template[match_result.group(1)] = match_result.group(2)

    print(template)

