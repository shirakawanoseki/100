
""" 言語処理100本ノック 2015 第5章: 係り受け解析
40. 係り受け解析結果の読み込み（形態素）
形態素を表すクラスMorphを実装せよ．このクラスは表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をメンバ変数に持つこととする．さらに，
CaboChaの解析結果（neko.txt.cabocha）を読み込み，各文をMorphオブジェクトのリストとして表現し，3文目の形態素列を表示せよ．
"""

import CaboCha
import re
import sys

class Morph:
    """ 形態素を表すクラス
    """
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self):
        return ('surface[{0}] base[{1}] pos[{2}] pos1[{3}]'.format(self.surface, self.base, self.pos, self.pos1))


def parse_input_file():
    """ 「我が輩は猫である」を係り受け解析して結果を'neko.txt.cabocha'に保存

    Args:
    　特になし
    Raise:
      特になし
    Return:
      解析結果を*.cabochaに保存
    Note:
    　入力ファイル名はコマンドライン引数より指定
    """

    CaboChaParser = CaboCha.Parser()

    with open(sys.argv[1], mode='r') as input_file, open(sys.argv[1] + '.cabocha', mode='w') as output_file:
        #CaboChaで係り受け解析を行い、結果を出力ファイルに保存
        for line in input_file:
            tree =  CaboChaParser.parse(line)
            output_file.write(tree.toString(CaboCha.FORMAT_LATTICE))

def build_morph_list():
    """ 「我が輩は猫である」を係り受け解析して結果を文毎のMorphオブジェクトのリストに保存

    Args:
    　特になし
    Raise:
      特になし
    Return:
      文毎のMorphオブジェクトのリスト
    Note:
    　入力ファイル名はコマンドライン引数より指定
    """
    sentence_list = []
    with open(sys.argv[1] + '.cabocha', mode='r') as input_file:
        morph_obj_list = []
        for line in input_file.readlines():
            
            #文の終端に達したら(EOSに達したら)次の文へ
            if re.match(r'^EOS$',line) or not line:
                sentence_list.append(morph_obj_list)
                morph_obj_list = []
                continue
            else:
                #*で始まる行は係り受け解析なので今回は無視
                if re.match(r'^\*',line):
                    continue

                #タブとカンマで区切られている本文を分解
                split_by_tab = line.split('\t')
                split_by_comma = split_by_tab[1].split(',')

                #Morphオブジェクトを作成して文毎のリストに追加
                morph_obj = Morph(split_by_tab[0], split_by_comma[6], split_by_comma[0], split_by_comma[1])
                morph_obj_list.append(morph_obj)

    return sentence_list


if __name__ == "__main__":

    #係り受け解析の実行と解析結果の保存
    parse_input_file()
    sentence_list = build_morph_list()

    #3番目の形態素列を表示
    for morph in sentence_list[2]:
        print(morph)

