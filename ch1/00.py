
""" 言語処理100本ノック 2015 第1章: 準備運動
00. 文字列の逆順
文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ。
"""

def reverse(arg):
    """ 引数に指定された文字列を逆に並べる。

    Args:
      arg: （末尾から先頭に向かって）逆に並べる文字列
    Raise:
      特になし
    Return:
      （末尾から先頭に向かって）逆に並べられた文字列
    """
    length = len(arg)
    reverse = ''
    while length != 0:
        reverse += s[length-1]
        length -= 1
    return reverse

def lreverse(arg):
    """ 引数に指定された文字列を逆に並べる（listクラスのreverseを使用）。

    Args:
      arg: （末尾から先頭に向かって）逆に並べる文字列
    Raise:
      特になし
    Return:
      （末尾から先頭に向かって）逆に並べられた文字列
    """
    larg = list(arg)
    larg.reverse()
    reverse = ''
    for e in larg:
        reverse += e
    return reverse

#
# 上記関数を呼び出し
#

s = "stressed"
print(reverse(s))
print(lreverse(s))

