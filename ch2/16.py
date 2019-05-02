
""" 言語処理100本ノック 2015 第2章: UNIXコマンドの基礎
16. ファイルをN分割する
自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．
"""

#
# 以下のようにsplitコマンドを使用して確認
# split -l 5 hightemp.txt
#

import sys
import math
import fileinput

with fileinput.input(files=(sys.argv[2])) as input:
    # ファイルの分割数をコマンドライン引数より取得
    n = int(sys.argv[1])

    # バッファにファイルの内容を読み込んでしまう
    file_buffer = []
    for line in input:
        file_buffer.append(line)
    
    # バッファの行数
    lines = len(file_buffer)

    # 各ファイルに出力する行数の算出
    output_lines = math.ceil(lines/n)

    offset = 0
    for fragment in range(0, n):
        #n個目
        output = open("fragment_{0}.txt".format(fragment), "w")
        for index in range(offset, offset+output_lines):
            if index < lines:
                print(file_buffer[index].rstrip("\r\n"), file=output)
        offset = offset + output_lines

