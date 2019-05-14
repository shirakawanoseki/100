
""" 言語処理100本ノック 2015 第4章: 形態素解析
37. 頻度上位10語
出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．
"""

import collections
import re
import sys
import matplotlib.pyplot as plt
import MeCab

def parse_input_file():
    """ 「我が輩は猫である」を形態素解析して結果を'neko.txt.mecab'に保存

    Args:
    　特になし
    Raise:
      特になし
    Return:
      特になし
    Note:
    　入力ファイルはコマンドライン引数より指定
    """
    with open(sys.argv[1], mode='r') as input_file, open('neko.txt.mecab', mode='w') as output_file:
        #入力ファイルの読み込み
        read_data = input_file.read()
        #MeCabで形態素解析を行い、結果を出力ファイルに保存
        mecab = MeCab.Tagger()
        output_file.write(mecab.parse(read_data))

def build_map_list():
    """ 「我が輩は猫である」の形態素解析結果のマップリストを作成して返却

    Args:
    　特になし
    Raise:
      特になし
    Return:
      形態素解析結果のマップリスト
    Note:
    　MeCabのバージョンによっては出力フォーマットが変わるかも。。
    """
    master_map_list = []
    with open('neko.txt.mecab', mode='r') as input_file:
        #マップのリスト
        map_list = []
        for line in input_file.readlines():

            #入力ファイルの終端に達したら(EOSに達したら)ループを抜ける
            if re.match(r'^EOS$',line) or not line:
                break

            #フォーマットに従って文を分解
            split_by_tab = line.split('\t')
            split_by_comma = split_by_tab[1].split(',')

            #句点に達したら文末と判定
            if split_by_comma[1] == '句点':
                master_map_list.append(map_list)
                map_list = []
                continue

            #形態素のマップを作成
            elements = {
                'surface':split_by_tab[0],
                'base':split_by_comma[6],
                'pos':split_by_comma[0],
                'pos1':split_by_comma[1],
            }

            map_list.append(elements)

    return master_map_list

if __name__ == "__main__":

    #形態素解析の実行と解析結果の保存
    parse_input_file()
    #形態素解析結果の読み込み
    master_map_list = build_map_list()

    #単語の出現数をカウント
    words_occur_freq = {}
    for master_map in master_map_list:
        for element_dic in master_map:
            if element_dic['surface'] in words_occur_freq:
                words_occur_freq[element_dic['surface']] = (int(words_occur_freq[element_dic['surface']]) + 1)
            else:
                words_occur_freq[element_dic['surface']] = int(1)

    #出現数が多い順にソート
    od = collections.OrderedDict(sorted(words_occur_freq.items(), key=lambda x: x[1], reverse=True))

    #グラフ出力用のデータを準備
    items = 0
    names = []
    values = []
    for k,v in od.items():
        if items < 10:
            names.append(k)
            values.append(v)
            items += 1

    #グラフの作成
    plt.figure(1)
    plt.bar(names,values)
    plt.suptitle('頻度上位10語')
    plt.show()

