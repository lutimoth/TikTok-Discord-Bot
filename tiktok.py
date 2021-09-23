from TikTokApi import TikTokApi

uId = "6940061807843591000"
secUid = "MS4wLjABAAAAvA6cxXvkBRrfcI7cQAW0eyZiT35H6XUiN_77y4PXOdKhMYfgAKfx7K2dKb2iIEZ1"
verifyFp = "verify_ktswr95c_mSSa5qC2_mvku_4S0x_9Hnn_oCUJAqVl9fvg"


user = "naturesbless"

api = TikTokApi.get_instance()
results = 10

posts = api.user_posts(uId, secUid, count=1)

for tiktok in posts:
    print('https://www.tiktok.com/@naturesbless/video/'+tiktok['video']['id'])

