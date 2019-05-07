
""" 言語処理100本ノック 2015 第3章: 正規表現
24. ファイル参照の抽出
記事から参照されているメディアファイルをすべて抜き出せ．
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
                search_result = re.search(r'(ファイル|[Ff]ile)\:((.*)\.(jpg|JPG|JPEG|jpeg|svg|png|PNG))', line)
                if search_result:
                    print("{0}".format(search_result.group(2)))


