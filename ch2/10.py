
""" 言語処理100本ノック 2015 第2章: UNIXコマンドの基礎
10. 行数のカウント
行数をカウントせよ．確認にはwcコマンドを用いよ．
"""

import sys
import fileinput

with fileinput.input(files=(sys.argv[1])) as input:
    line_count = 0
    for line in input:
        line_count += 1
    print('\t' + str(line_count) + ' ' + sys.argv[1])
