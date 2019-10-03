import json
import tweepy
import asyncio
from unidecode import unidecode
from decouple import config

def robotTwitter(content):
    return contentFromTwitter(content)
    
#def contentFromTwitter(content):
def contentFromTwitter(content):
    consumer_key=config('consumer_key')
    consumer_secret=config('consumer_secret')
    access_token=config('access_token')
    access_token_secret=config('access_token_secret')

    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True)

    search = api.search(q=content, lang='pt', since ='2019-01-01', until = '2019-10-03')

    tweets = []

    for t in search:
        data = {
            'text': t.text,
            'user': t.user.screen_name,
            'location': t.user.location,
            'place': t.place,
            #'geo_id': t.geo_id,
            'followers_count': t.user.followers_count,
            'verified': t.user.verified,
            'created_at': t.created_at
        }

        tweets.append(data)

    return tweets