""" 言語処理100本ノック 2015 第3章: 正規表現
22. カテゴリ名の抽出
記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．
"""

import sys
import json
import gzip
import re

with gzip.open(sys.argv[1], "rt") as f:
    for data_line in f:
        js = json.loads(data_line)
        splited_json = js["text"].split('\n')
        for line in splited_json:
            search_result = re.search(r'^\[\[Category:(.*)\]\]$', line)
            if search_result:
                print(search_result.group(1))