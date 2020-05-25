# モジュールのインポート
import config
import dmm
import json
import pprint

# API ID と アフィリエイトIDをセット

api_id = config.API
affiliate_id = config.ID

# インスタンスの作成
api = dmm.API(api_id=api_id, affiliate_id=affiliate_id)

def getFanzaItem(arg):
    item_search = api.item_search(site="FANZA", hits=3, keyword=arg)
    return item_search
