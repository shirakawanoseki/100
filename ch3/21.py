""" 言語処理100本ノック 2015 第3章: 正規表現
21. カテゴリ名を含む行を抽出
記事中でカテゴリ名を宣言している行を抽出せよ．
"""

import sys
import json
import gzip
import re

with gzip.open(sys.argv[1], "rt") as f:
    for data_line in f:
        js = json.loads(data_line)
        if js["title"] == 'イギリス':
            splited_json = js["text"].split('\n')
            for line in splited_json:
                if re.match(r'^\[\[Category:(.*)\]\]$', line):
                    print(line)
