
""" 言語処理100本ノック 2015 第1章: 準備運動
04. 元素記号
"Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目
の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．
"""


def create_periodic_table(str):
    """ 引数に指定された文字列の単語の先頭の1文字or2文字を抽出して周期表の連想配列を作成
    Args:
      str: 任意の英文の文字列(元素記号が頭文字となる単語で構成されていること)
    Raise:
      特になし
    Return:
      周期表の連想配列
    Note:
    　二文字中絀のインデックスは埋め込まない方がいいかなあ？
    """
    index = 1
    index_dictionary = {}
    for word in str.split(' '):
        #print("{0} -> {1}".format(word, index))
        if index in (1, 5, 6, 7, 8, 9, 15, 16, 19):
            index_dictionary[word[0]] = index
        else:
            index_dictionary[word[0:2]] = index
        index += 1
    return index_dictionary

#
# 関数の呼び出し
#

str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
print(create_periodic_table(str))

