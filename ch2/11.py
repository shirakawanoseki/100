
""" 言語処理100本ノック 2015 第2章: UNIXコマンドの基礎
11. タブをスペースに置換
タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
"""

#
# 以下のようにexpandコマンドを使用して確認
# expand -t 1 hightemp.txt > result.txt 
#

import sys
import fileinput

with fileinput.input(files=(sys.argv[1])) as input:
    for line in input:
        listed_line = list(line)
        joined_line = []
        for x in listed_line:
            if x == '\t':
                joined_line.append(' ')
            else:
                joined_line.append(x)
        print(''.join(joined_line), end="")

