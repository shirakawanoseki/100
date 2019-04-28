
""" 言語処理100本ノック 2015 第1章: 準備運動
03. 円周率
"Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."という文を単語に分解し，各単語の（アルファベットの
）文字数を先頭から出現順に並べたリストを作成せよ．
"""


def count_alphabets(str):
    """ 引数に指定された文字列に含まれる単語のアルファベット数を文字列中の出現順にリスト
    Args:
      str: 任意の英文の文字列
    Raise:
      特になし
    Return:
      単語に含まれるアルファベット数のリスト
    Note:
    """
    splited_str = str.split(' ')
    result_list = []
    for word in splited_str:
        alphabets = list(word)
        alphabets_count = 0
        for alphabet in alphabets:
            #アルファベットの場合にのみカウント
            if alphabet.isalpha():
                alphabets_count += 1
        result_list.append(alphabets_count)
    return result_list

#
# 関数の呼び出し
#

str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
print(count_alphabets(str))

