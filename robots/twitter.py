import json
import sys
import re
import tweepy
import asyncio
from decouple import config
import jsonpickle

def robotTwitter(content):
    return downloadTweets(content)
    #return contentFromTwitter(content)
    

def downloadTweets(content):
    consumer_key=config('consumer_key')
    consumer_secret=config('consumer_secret')

    auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    if (not api):
        print ('Não é possível autenticar')
        sys.exit(-1)

    searchQuery = content  # é isso que estamos procurando
    maxTweets = 100 # Algum número grande e arbitrário
    tweetsPerQry = 100  # este é o máximo que a API permite
    fName = 'tweets.json' # Armazenaremos os tweets em um arquivo de texto.

    # Se os resultados de um ID específico em diante forem solicitados, defina since_id para esse ID.
    # else padrão para nenhum limite inferior, volte o quanto a API permitir
    sinceId = None

    # Se houver apenas resultados abaixo de um ID específico, defina max_id para esse ID.
    # else padrão para nenhum limite superior, comece pelo tweet mais recente correspondente à consulta de pesquisa.
    max_id = -1

    tweetCount = 0
    print('Baixando o máximo de {} tweets com o termo {}'.format(maxTweets, content.upper()))
    with open(fName, 'w') as f:
        while tweetCount < maxTweets:
            try:
                if (max_id <= 0):
                    if (not sinceId):
                        new_tweets = api.search(q=searchQuery, count=tweetsPerQry, lang='pt')
                    else:
                        new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                                since_id=sinceId, lang='pt')
                else:
                    if (not sinceId):
                        new_tweets = api.search(q=searchQuery, count=tweetsPerQry, lang='pt',
                                                max_id=str(max_id - 1))
                    else:
                        new_tweets = api.search(q=searchQuery, count=tweetsPerQry, lang='pt',
                                                max_id=str(max_id - 1),
                                                since_id=sinceId)
                if not new_tweets:
                    print('Não foram encontrados mais tweets')
                    break
                for tweet in new_tweets:
                    f.write(jsonpickle.encode(tweet._json, unpicklable=False) + '\n')
                tweetCount += len(new_tweets)
                print('Já baixou {} tweets'.format(tweetCount))
                max_id = new_tweets[-1].id
            except tweepy.TweepError as e:
                print('Algum erro em: ' + str(e))
                break

    print('Baixados {} tweets, salvos em {}'.format(tweetCount, fName))

"""
    for page in tweepy.Cursor(api.search, q=content, lang='pt', Tweet_mode='extended', result_type ='recent', count=100).pages(5):

        print('Buscando tweets com o termo {}...'.format(content.upper()))
        
        data = {
            'text': page[0]._json['text'],
            'user': page[0]._json['user']['screen_name'],
            'location': page[0]._json['user']['location'],
            'place': page[0]._json['place'],
            'followers_count': page[0]._json['user']['followers_count'],
            'verified': page[0]._json['user']['verified'],
            'created_at': page[0]._json['created_at']
        }

        tweets.append(data)
    
    search = api.search(q=content, lang='pt', count=100)

    for t in search:
        data = {
            'text': t.text,
            'user': t.user.screen_name,
            'location': t.user.location,
            'place': t.place,
            'followers_count': t.user.followers_count,
            'verified': t.user.verified,
            'created_at': t.created_at
        }

        tweets.append(data)
"""

def clean_tweet(tweet):
    
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|      (\w+:\/\/\S+)", " ", tweet).split())