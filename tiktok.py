from TikTokApi import TikTokApi

# Initialize the TikTok instance
api = TikTokApi.get_instance()

# Ask for their username
user = input("Enter your username: ")

# Get TikTok Dictionary for most recent (1) video
userInfo = api.by_username(user, count=1)

# Print direct link to most recent Tik Tok
for tiktok in userInfo:
    print('https://www.tiktok.com/@'+user+'/video/'+tiktok['id'])

