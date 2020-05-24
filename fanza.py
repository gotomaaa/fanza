# モジュールのインポート
import config
import dmm

# API ID と アフィリエイトIDをセット

api_id = config.API
affiliate_id = config.ID

# インスタンスの作成
api = dmm.API(api_id=api_id, affiliate_id=affiliate_id)


item_search = api.item_search(site="FANZA", hits=1, keyword="ロリ")

print(item_search)
