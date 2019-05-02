
""" 言語処理100本ノック 2015 第2章: UNIXコマンドの基礎
15. 末尾のN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．
"""

#
# 以下のようにtailコマンドを使用して確認
# tail -n 5 hightemp.txt
#

import sys
import fileinput

with fileinput.input(files=(sys.argv[2])) as input:
    # 表示する行数をコマンドライン引数より取得
    n = int(sys.argv[1])

    # バッファにファイルの内容を読み込んでしまう
    file_buffer = []
    for line in input:
        file_buffer.append(line)
    
    # バッファの行数から表示行を引いた行から最後の行までを表示
    lines = len(file_buffer)
    for line in range(lines - n, lines):
        print(file_buffer[line], end="")
