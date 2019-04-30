
""" 言語処理100本ノック 2015 第1章: 準備運動
08. 暗号文
与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
・英小文字ならば(219 - 文字コード)の文字に置換
・その他の文字はそのまま出力
この関数を用い，英語のメッセージを暗号化・復号化せよ．
"""

def cipher(sentence):
    """ 指定された文字列の暗号化および復号化
    Args:
      sentence: 暗号化および復号化の対象となる文字列
    Raise:
      特になし
    Return:
      暗号化・復号化の結果文字列
    Note:
    　特になし
    """
    encoded = []
    for alphabet in list(sentence):
        if alphabet.isalpha() and alphabet.islower():
            encoded.append(chr(219 - ord(alphabet)))
        else:
            encoded.append(alphabet)
    return ''.join(encoded)

#
# 関数の呼び出し
#

org_sentence = "Hello, World!"

#暗号化
print(cipher(org_sentence))

#復号化
print(cipher(cipher(org_sentence)))
