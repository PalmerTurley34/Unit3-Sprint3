# web_app/services/twitter_service.py

import tweepy
import os
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
print("AUTH", type(auth))
api = tweepy.API(auth)
print("API CLIENT", type(api))

# user = api.get_user('bayleemarie10')
# tweets = api.user_timeline('bayleemarie10', tweet_mode='extended', count=50, exclude_replies=True, include_rts=True)
# for tweet in tweets:
#     print(tweet.full_text)

#def twitter_api_client():
#    return tweepy.API(auth)

# def twitter_api():
#     auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
#     auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
#     print("AUTH", auth)
#     api = tweepy.API(auth)
#     print("API", api)
#     #print(dir(api))
#     return api

# if __name__ == "__main__":

#     api = twitter_api()
#     user = api.get_user("elonmusk")
#     print("USER", user)
#     print(user.screen_name)
#     print(user.name)
#     print(user.followers_count)