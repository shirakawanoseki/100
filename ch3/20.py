
""" 言語処理100本ノック 2015 第3章: 正規表現
20. JSONデータの読み込み
Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．問題21-29では，ここで抽出した記事本文に対して実行せよ．．
"""

import sys
import json
import gzip

with gzip.open(sys.argv[1], "rt") as f:
    for data_line in f:
        js = json.loads(data_line)
        if js["title"] == 'イギリス':
            print(js["text"])
            break

