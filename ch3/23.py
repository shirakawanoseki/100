
""" 言語処理100本ノック 2015 第3章: 正規表現
23. セクション構造
記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．
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
            search_result = re.search(r'^\={5}\s*(.*)\s*\={5}$', line)
            if search_result:
                print("{0} {1}".format(search_result.group(1),4))
                continue
            search_result = re.search(r'^\={4}\s*(.*)\s*\={4}$', line)
            if search_result:
                print("{0} {1}".format(search_result.group(1),3))
                continue
            search_result = re.search(r'^\={3}\s*(.*)\s*\={3}$', line)
            if search_result:
                print("{0} {1}".format(search_result.group(1),2))
                continue
            search_result = re.search(r'^\={2}\s*(.*)\s*\={2}$', line)
            if search_result:
                print("{0} {1}".format(search_result.group(1),1))
                continue
