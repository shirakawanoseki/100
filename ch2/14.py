
""" 言語処理100本ノック 2015 第2章: UNIXコマンドの基礎
14. 先頭からN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．
"""
#
# 以下のようにheadコマンドを使用して確認
# head -n 5 hightemp.txt
#

import sys
import fileinput

with fileinput.input(files=(sys.argv[2])) as input:
    n = int(sys.argv[1])
    count = 0
    for line in input:
        if count < n:
            print(line, end="")
        count += 1

