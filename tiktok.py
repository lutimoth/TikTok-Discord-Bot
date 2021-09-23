from TikTokApi import TikTokApi

verifyFp = "verify_ktswr95c_mSSa5qC2_mvku_4S0x_9Hnn_oCUJAqVl9fvg"

user = "naturesbless"

api = TikTokApi.get_instance()
results = 10

trending = api.by_trending(count = results, custom_verifyFp = verifyFp)

for tiktok in trending:
    print (tiktok['id'])

print(len(trending))
