
""" 言語処理100本ノック 2015 第2章: UNIXコマンドの基礎
17. １列目の文字列の異なり
1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．
"""

#
# 以下のようにcut,sort,uniqコマンドを使用して確認
# cut -f 1 hightemp.txt | sort | uniq
#

import sys
import math
import fileinput

with fileinput.input(files=(sys.argv[1])) as input:
    result_set = set()
    for line in input:
        splited_line = line.split('\t')
        if splited_line[0] not in result_set:
            result_set.add(splited_line[0])
    
    for x in result_set:
        print(x)
