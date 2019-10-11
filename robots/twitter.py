# -*- Coding: UTF-8 -*-
#coding: utf-8

import json
import sys
import re
import tweepy
from decouple import config
<<<<<<< HEAD
from unicodedata import normalize
=======
>>>>>>> 36d599ae7b7f83083f44dffdb1d9614d542f3b9b


def downloadTweets(content):
    consumer_key=config('consumer_key')
    consumer_secret=config('consumer_secret')

    auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    if (not api):
        print ('Não é possível autenticar')
        sys.exit(-1)

    searchQuery = content  # é isso que estamos procurando
<<<<<<< HEAD
    maxTweets = 3 # Algum número grande e arbitrário
    tweetsPerQry = 3  # este é o máximo que a API permite 100
=======
    maxTweets = 5 # Algum número grande e arbitrário
    tweetsPerQry = 5  # este é o máximo que a API permite 100
>>>>>>> 36d599ae7b7f83083f44dffdb1d9614d542f3b9b

    # Se os resultados de um ID específico em diante forem solicitados, defina since_id para esse ID.
    # else padrão para nenhum limite inferior, volte o quanto a API permitir
    sinceId = None

    # Se houver apenas resultados abaixo de um ID específico, defina max_id para esse ID.
    # else padrão para nenhum limite superior, comece pelo tweet mais recente correspondente à consulta de pesquisa.
    max_id = -1

    tweetCount = 0
    print('Baixando os tweets com o termo {}'.format(content.upper()))

    tweets_list = []

    while tweetCount < maxTweets:
        try:
            if (max_id <= 0):
                if (not sinceId):
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry, 
                                            Tweet_mode='extended', lang='pt')
<<<<<<< HEAD
                else:
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry, Tweet_mode='extended',
                                            since_id=sinceId, lang='pt')
            else:
                if (not sinceId):
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry, lang='pt',
                                            Tweet_mode='extended', max_id=str(max_id - 1))
                else:
=======
                else:
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry, Tweet_mode='extended',
                                            since_id=sinceId, lang='pt')
            else:
                if (not sinceId):
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry, lang='pt',
                                            Tweet_mode='extended', max_id=str(max_id - 1))
                else:
>>>>>>> 36d599ae7b7f83083f44dffdb1d9614d542f3b9b
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry, lang='pt',
                                            Tweet_mode='extended', max_id=str(max_id - 1),
                                            since_id=sinceId)
            if not new_tweets:
                print('Não foram encontrados mais tweets')
                break

            for tweet in new_tweets:

<<<<<<< HEAD
                data = {
                    'user_id': tweet.user.id_str,
                    'user': tweet.user.screen_name,
                    'text': tweet.text,
                    'text_sanitized': clean_tweet(tweet.text),
                    'location': tweet.user.location,
                    'place': tweet.place,
                    'coordinates': tweet.coordinates,
                    'followers_count': tweet.user.followers_count,
                    'verified': tweet.user.verified,
                    'created_at': tweet.created_at,
                }

=======
                tweet_lat = 0.0
                tweet_lon = 0.0

                if tweet._json['coordinates']:    
                    geo = tweet['coordinates']
                    if not geo is None:
                        latlon = geo['coordinates']
                        tweet_lon = latlon[0]
                        tweet_lat = latlon[1]

                data = {
                    'user_id': tweet.user.id,
                    'user': tweet.user.screen_name,
                    'text': tweet.text,
                    'text_sanitized': clean_tweet(tweet.text),
                    'location': tweet.user.location,
                    'place': tweet.place,
                    'tweet_lon': tweet_lon,
                    'tweet_lat': tweet_lat,
                    'followers_count': tweet.user.followers_count,
                    'verified': tweet.user.verified,
                    'created_at': tweet.created_at,
                }

>>>>>>> 36d599ae7b7f83083f44dffdb1d9614d542f3b9b
                tweets_list.append(data)

            tweetCount += len(new_tweets)
            print('Já baixou {} tweets'.format(tweetCount))
            max_id = new_tweets[-1].id

        except tweepy.TweepError as e:
            print('Algum erro em: ' + str(e))
            break

    print('Baixados {} tweets!'.format(tweetCount))

    return tweets_list


def clean_tweet(tweet):
    
<<<<<<< HEAD
    return removeBlankLine(removeRTArrobaLink(removeEmoji(removeAcentos(tweet))))
=======
    return removeBlankLine(removeRTArrobaLink(removeEmoji(tweet)))
>>>>>>> 36d599ae7b7f83083f44dffdb1d9614d542f3b9b

def removeBlankLine(text):
    allLines = text.split('\n')
    withoutBlankLine = list(filter(lambda line: len(line.strip()) != 0, allLines))

    return ' '.join(withoutBlankLine)

def removeRTArrobaLink(text):
    withoutArroba = re.sub(r'@\S+', '', text)
    withoutLink = re.sub(r'http\S+', '', withoutArroba)

    return withoutLink.replace('RT','')\
                                        .replace('.','')\
                                        .replace(',','')\
                                        .replace('-','')\
                                        .replace('  ',' ')\
                                        .replace('🤣','')\
                                        .strip()

def removeEmoji(text):
    emoji_pattern = re.compile('['
                            u'\U0001F600-\U0001F64F'  # emoticons
                            u'\U0001F300-\U0001F5FF'  # symbols & pictographs
                            u'\U0001F680-\U0001F6FF'  # transport & map symbols
                            u'\U0001F1E0-\U0001F1FF'  # flags (iOS)
                            u'\U00002702-\U000027B0'
                            u'\U000024C2-\U0001F251'
                            ']+', flags=re.UNICODE)

<<<<<<< HEAD
    return emoji_pattern.sub(r'', text)


def removeAcentos(text):
    
    return normalize('NFKD', text).encode('ASCII', 'ignore').decode('ASCII')
=======
    return emoji_pattern.sub(r'', text)
>>>>>>> 36d599ae7b7f83083f44dffdb1d9614d542f3b9b
