
""" 言語処理100本ノック 2015 第3章: 正規表現
28. MediaWikiマークアップの除去
27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，国の基本情報を整形せよ．
"""

import sys
import json
import gzip
import re

with gzip.open(sys.argv[1], "rt") as f:
    template = {}
    for data_line in f:
        js = json.loads(data_line)
        if js["title"] == 'イギリス':
            #基礎情報のセクションを先読
            basic_info = re.search(r'^\{\{基礎情報 国(.+?)\}\}$', js["text"], flags = (re.MULTILINE | re.DOTALL))
            #改行文字で分割
            splitted_basic_info = basic_info.group(0).split('\n')
            #分割した各行の内、パターンにマッチするものを辞書オブジェクトに格納
            for basic_info_line in splitted_basic_info:
                match_result = re.match(r'\|(.*?)\s+=\s+(.*)', basic_info_line)
                if match_result:
                    #マークアップの除去（可能な限り）
                    sub_result = re.sub(r'\[\[|\]\]|\{\{|\}\}|<ref(.*)(ref>|/>)|<br(\s*)/>|\'\'\'|ファイル:(.*)\|(.*)\||\(&(.*);\)|lang\|(.*)\|', '', match_result.group(2))
                    template[match_result.group(1)] = sub_result

    #print(template)
    for k,v in template.items(): print('{0} --> {1}'.format(k,v))
