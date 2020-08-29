import tweepy
import time
from _keys import consumer_key
from _keys import consumer_secret
from _keys import key
from _keys import secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


user = api.me()

search = 'Java'
numTweets = 5

for tweet in tweepy.Cursor(api.search, search).items(numTweets):
    try:
        print('Tweet Liked')
        tweet.favorite()
        tweet.retweet()
        time.sleep(1)
    except tweepy.error.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

for follower in tweepy.Cursor(api.followers).items():
    if follower.name == 'Elon Musk':
        follower.follow()
