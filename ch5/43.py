
""" 言語処理100本ノック 2015 第5章: 係り受け解析
43. 名詞を含む文節が動詞を含む文節に係るものを抽出
名詞を含む文節が，動詞を含む文節に係るとき，これらをタブ区切り形式で抽出せよ．ただし，句読点などの記号は出力しないようにせよ．
"""

import CaboCha
import re
import sys

class Morph:
    """
    形態素を表すクラス
    """
    def __init__(self, surface, base, pos, pos1):
        #表層系
        self.surface = surface
        #原型
        self.base = base
        #品詞
        self.pos = pos
        #品詞細分類1(3まである)
        self.pos1 = pos1

    def __str__(self):
        return ('surface[{0}] base[{1}] pos[{2}] pos1[{3}]'.format(self.surface, self.base, self.pos, self.pos1))

class Chunk:
    """
    文節を表すクラス
    """
    def __init__(self):
        self.morphs = [] #Morphクラスのインスタンスのリスト
        self.dst = -1 #係り先文節インデックス番号
        self.srcs = [] #係り元文節インデックス番号のリスト

    def check_pos(self, pos):
        """ 形態素クラス(Morph)の品詞のチェック
        Args:
            品詞（名詞、動詞、形容詞など）
        Raise:
            特になし
        Return:
            True -> 引数に指定された品詞 / False -> 引数に指定された品詞ではない
        Note:
    　      特になし
        """
        for morph in self.morphs:
            if morph.pos == pos: return True
        else: return False
    
    def normalize_surface(self):
        """ 表層系を表示用に正規化
        Args:
            特になし
        Raise:
            特になし
        Return:
            正規化された表層系（。、などの記号は除く）
        Note:
    　      特になし
        """
        surface = ''
        for morph in self.morphs:
            if morph.pos != '記号':
                surface = surface + morph.surface
        return surface

    def __str__(self):
        surface = ''
        for morph in self.morphs:
            surface += morph.surface
        return '{}\tsrcs{}\tdst[{}]'.format(surface, self.srcs, self.dst)

def parse_input_file():
    """
    「我が輩は猫である」を係り受け解析して結果を'neko.txt.cabocha'に保存
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

def chunk_obj_list():
    """
    「我が輩は猫である」を係り受け解析結果を読み出して1文毎にChunkクラスのリストを返す
    Args:
    　特になし
    Raise:
      StopIteration
    Return:
      1文毎のChunkクラスのリスト
    Note:
    　参照：https://qiita.com/segavvy/items/003e8b7e0f132f4fde1b
    """

    with open(sys.argv[1] + '.cabocha', mode='r') as input_file:

        chunk_dic = dict()
        idx = -1

        for line in input_file:

            if re.match(r'^EOS$',line):
                #文の終端に達したら(EOSに達したら)次の文へ
                if len(chunk_dic) > 0:
                    sorted_chunk_list = sorted(chunk_dic.items(), key=lambda x: x[0])
                    yield list(zip(*sorted_chunk_list))[1]
                    chunk_dic.clear()
                else:
                    yield []

            elif re.match(r'^\*',line):
                #文節区切り情報を分解して、係り先文節インデックス番号と係り元文節インデックス番号を取得
                split_by_space = line.split(' ')
                idx = int(split_by_space[1])
                dst = int(re.search(r'(.*?)D', split_by_space[2]).group(1))

                #Chunkがなければ生成し、係先のインデックスをセット
                if idx not in chunk_dic:
                    chunk_dic[idx] = Chunk()
                chunk_dic[idx].dst = dst

                #係先のChunkがなければ生成し、係先のインデックスを配列に追加
                if dst != -1:
                    if dst not in chunk_dic:
                        chunk_dic[dst] = Chunk()
                    chunk_dic[dst].srcs.append(idx)

            else:
                #タブとカンマで区切られている本文を分解
                split_by_tab = line.split('\t')
                split_by_comma = split_by_tab[1].split(',')

                #Morphオブジェクトを作成して文毎のリストに追加
                morph_obj = Morph(split_by_tab[0], split_by_comma[6], split_by_comma[0], split_by_comma[1])
                chunk_dic[idx].morphs.append(morph_obj)

        #raise StopIteration
 
if __name__ == "__main__":

    #係り受け解析の実行と解析結果の保存
    parse_input_file()

    # 1文ずつリスト作成
    for chunks in chunk_obj_list():
        
        for chunk in chunks:
            if chunk.dst != -1:

                if chunk.check_pos('名詞') and chunks[chunk.dst].check_pos('動詞'):
                    source = chunk.normalize_surface()
                    dest = chunks[chunk.dst].normalize_surface()
                    if source != '' and dest != '':
                        print('{}\t{}'.format(source, dest))

