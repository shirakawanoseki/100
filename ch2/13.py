
""" 言語処理100本ノック 2015 第2章: UNIXコマンドの基礎
13. col1.txtとcol2.txtをマージ
12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．
"""
#
# 以下のようにpasteコマンドを使用して確認
# paste -d '\t' col1.txt col2.txt
#

import sys
import fileinput

result = open("merge.txt", "w")

with fileinput.input(files=(sys.argv[1])) as input_1, fileinput.input(files=(sys.argv[2])) as input_2:
    col1_list = []
    for line_1 in input_1:
        col1_list.append(line_1)
    
    col2_list = []
    for line_2 in input_2:
        col2_list.append(line_2)
    
    for index in range(len(col1_list)):
        print("{0}\t{1}".format(col1_list[index].rstrip("\r\n"), col2_list[index].rstrip("\r\n")), file=result)
