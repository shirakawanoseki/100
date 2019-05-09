
""" 言語処理100本ノック 2015 第3章: 正規表現
29. 国旗画像のURLを取得する
テンプレートの内容を利用し，国旗画像のURLを取得せよ．（ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）
"""

import sys
import json
import gzip
import re
import requests

with gzip.open(sys.argv[1], "rt") as f:
    #template = {}
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
                if match_result and match_result.group(1) == '国旗画像':
                    #マークアップの除去（可能な限り）
                    edit_result = re.sub(r'\[\[|\]\]|\{\{|\}\}|<ref(.*)(ref>|/>)|<br(\s*)/>|\'\'\'|ファイル:(.*)\|(.*)\||\(&(.*);\)|lang\|(.*)\|', '', match_result.group(2))
                    #MediaWiki API(imageinfo)を実行して英国国旗画像のurlを取得
                    session = requests.Session()

                    URL = "https://www.mediawiki.org/w/api.php"

                    PARAMS = {
                        "action":"query",
                        "format":"json",
                        "prop": "imageinfo",
                        "titles":"File:{0}".format(edit_result),
                        "iiprop":"url"
                    }

                    session_response = session.get(url=URL, params=PARAMS)
                    DATA = session_response.json()

                    print(DATA['query']['pages']['-1']['imageinfo'][0]['url'])
