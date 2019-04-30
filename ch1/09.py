
""" 言語処理100本ノック 2015 第1章: 準備運動
09. Typoglycemia
スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．ただし，長さが４以下の単語は並
び替えないこととする．適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ．
"""

import random

def typoglycemia(sentence):
    """ 長さが4以上の単語の文字を先頭と末尾を残してランダムに並びかえる。
    Args:
      sentence: 単語の並び替え対象となる文字列
    Raise:
      特になし
    Return:
      対象となる単語の文字の並べ替えを行った結果文字列
    Note:
    　特になし
    """
    splited_sentence = sentence.split(' ')
    result = []
    for word in splited_sentence:
        if 4 < len(word):
            listed_word = list(word)
            listed_word[1:len(word) - 1] = random.sample(listed_word[1:len(word) - 1],len(word) - 2)
            result.append(''.join(listed_word))
        else:
            result.append(word)
    return ' '.join(result)

#
# 関数の呼び出し
#

org_sentence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(typoglycemia(org_sentence))
