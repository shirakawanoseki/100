
""" 言語処理100本ノック 2015 第1章: 準備運動
02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
"""

str01 = 'パトカー'
str02 = 'タクシー'

def MutualConnection(str01, str02):
    """ 引数に指定された文字列から一文字ずつ抜き出して交互に並べる。

    Args:
      str01: 交互に並べる文字列（一つ目）
      str02: 交互に並べる文字列（二つ目）
    Raise:
      特になし
    Return:
      二つの文字列から一文字ずつ抜き出して交互に並べた文字列
    Note:
    　引数に指定される文字列の長さは同一であることを前提として実装されている点に注意
    """
    str01_length = len(str01)
    str02_length = len(str02)
    str_common_index = 0
    m_connected_str = ''
    while str_common_index < str01_length and str_common_index < str02_length:
        m_connected_str = m_connected_str + str01[str_common_index] + str02[str_common_index]
        str_common_index = str_common_index + 1
    return m_connected_str

#
# 処理の呼び出し
#
print(MutualConnection(str01, str02))

