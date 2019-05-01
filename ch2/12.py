
""" 言語処理100本ノック 2015 第2章: UNIXコマンドの基礎
12. 1列目をcol1.txtに，2列目をcol2.txtに保存
各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．
"""

import sys
import fileinput

col1 = open("col1.txt", "w")
col2 = open("col2.txt", "w")

with fileinput.input(files=(sys.argv[1])) as input:
    for line in input:
        splited_line = line.split('\t')
        print(splited_line[0], file=col1)
        print(splited_line[1], file=col2)
