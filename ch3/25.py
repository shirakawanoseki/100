
""" 言語処理100本ノック 2015 第3章: 正規表現
25. テンプレートの抽出
記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．
"""

import sys
import json
import gzip
import re

with gzip.open(sys.argv[1], "rt") as f:
    for data_line in f:
        js = json.loads(data_line)
        if js["title"] == 'イギリス':
            json_text = js["text"]
            search_result = re.finditer(r'^\{\{基礎情報 国(.+?)\}\}$', json_text, flags = (re.MULTILINE | re.DOTALL))
            for r in search_result:
                print(r.group(0))
