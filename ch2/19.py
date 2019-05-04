
""" 言語処理100本ノック 2015 第2章: UNIXコマンドの基礎
19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．
"""

#
# 以下のようにcut,sort,uniqコマンドを使用して確認
# cut -f 1 hightemp.txt | sort | uniq
#

import sys
import fileinput
import collections

with fileinput.input(files=(sys.argv[1])) as input:
    frequency_dic = {}
    for line in input:
        splited_line = line.split('\t')
        if splited_line[0] not in frequency_dic:
            frequency_dic[splited_line[0]] = 1
        else:
            frequency_dic[splited_line[0]] += 1
    
    od = collections.OrderedDict(sorted(frequency_dic.items(), key=lambda x: x[1], reverse=True))
    for key, value in od.items():
        print(key,value)

