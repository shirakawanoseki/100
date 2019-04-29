
""" 言語処理100本ノック 2015 第1章: 準備運動
06. 集合
"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに
含まれるかどうかを調べよ．
"""

def n_gram(text_sequence, n):
    """ (05と共通)与えられたシーケンス（文字列やリストなど）からn-gramを作成
    Args:
      str: 任意のシーケンス（文字列やリストなど）
      n: n-gramのn
    Raise:
      特になし
    Return:
      n-gram(リスト形式)
    Note:
    　特になし
    """
    n_gram = []
    sequence_index = 0

    while sequence_index < len(text_sequence):
        n_gram_element = text_sequence[sequence_index:sequence_index+n]
        if len(n_gram_element) == n:
            n_gram.append(n_gram_element)
        sequence_index += 1
    return n_gram

#
# 関数の呼び出し
#

str_seq_1 = "paraparaparadise"
str_seq_2 = "paragraph"

X = frozenset(n_gram(str_seq_1,2))
Y = frozenset(n_gram(str_seq_2,2))

#frozenset({'ap', 'pa', 'ar', 'ad', 'di', 'se', 'is', 'ra'})
#frozenset({'ap', 'ph', 'pa', 'ar', 'ag', 'gr', 'ra'})

#和集合
print(X.union(Y))

#積集合
print(X.intersection(Y))

#差集合
print(X.difference(Y))

#'se'というbi-gramがXおよびYに含まれるかどうか
print('se' in X)
print('se' in Y)
