
""" 言語処理100本ノック 2015 第2章: UNIXコマンドの基礎
18. 各行を3コラム目の数値の降順にソート
各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．確認にはsortコマンドを用いよ
（この問題はコマンドで実行した時の結果と合わなくてもよい）．
"""

#
# 以下のようにsortコマンドを使用して確認
# sort -k 2 hightemp.txt
#

import sys
import fileinput

with fileinput.input(files=(sys.argv[1])) as input:
    list_of_list = []
    for line in input:
        splited_line = line.split('\t')
        list_of_list.append(splited_line)

    list_of_list.sort(key=lambda x: x[2], reverse=True)

    for element in list_of_list:
        print("{0}\t{1}\t{2}\t{3}".format(element[0],element[1],element[2],element[3],), end="")
    


