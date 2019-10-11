import json
import sys
import re
import tweepy
from decouple import config
import pandas as pd


consumer_key=config('consumer_key')
consumer_secret=config('consumer_secret')

auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

if (not api):
    print ('Não é possível autenticar')
    sys.exit(-1)

content = 'neymar'

searchQuery = content  # é isso que estamos procurando
maxTweets = 2 # Algum número grande e arbitrário
tweetsPerQry = 2  # este é o máximo que a API permite 100

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
            else:
                new_tweets = api.search(q=searchQuery, count=tweetsPerQry, Tweet_mode='extended',
                                        since_id=sinceId, lang='pt')
        else:
            if (not sinceId):
                new_tweets = api.search(q=searchQuery, count=tweetsPerQry, lang='pt',
                                        Tweet_mode='extended', max_id=str(max_id - 1))
            else:
                new_tweets = api.search(q=searchQuery, count=tweetsPerQry, lang='pt',
                                        Tweet_mode='extended', max_id=str(max_id - 1),
                                        since_id=sinceId)
        if not new_tweets:
            print('Não foram encontrados mais tweets')
            break

        for tweet in new_tweets:  

            tweets_list.append(tweet._json['text'])
            
        tweetCount += len(new_tweets)
        print('Já baixou {} tweets'.format(tweetCount))
        max_id = new_tweets[-1].id

    except tweepy.TweepError as e:
        print('Algum erro em: ' + str(e))
        break

print('Baixados {} tweets!'.format(tweetCount))

dataSet = pd.DataFrame()

def resolveAcento(text):
    pass

from unicodedata import normalize

def remover_acentos(txt):
     return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')

dataSet['text'] = [remover_acentos(i) for i in tweets_list]

dataSet.to_csv('dataSet-teste.csv', sep=';')

print(tweets_list)

