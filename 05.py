
""" 言語処理100本ノック 2015 第1章: 準備運動
05. n-gram
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
"""

def n_gram(text_sequence,n):
    """ 与えられたシーケンス（文字列やリストなど）からn-gramを作成
    Args:
      text_sequence: 任意のシーケンス（文字列やリストなど）
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

text_sequence = "I am an NLPer"
splited_text_sequence = text_sequence.split(' ')

# 単語bi-gram
print(n_gram(splited_text_sequence,2))
# 文字bi-gram
print(n_gram(text_sequence, 2))
