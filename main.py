<<<<<<< HEAD
# -*- Coding: UTF-8 -*-
#coding: utf-8

import robots.twitter as robot
from robots.watson import sentimentWatson, keywordsWatson
import pandas as pd
=======
import robots.twitter as robot
from robots.watson import sentimentWatson, keywordsWatson
>>>>>>> 36d599ae7b7f83083f44dffdb1d9614d542f3b9b

def main():
    # cria dicionário de dados e sua estrutura
    content = {}

    content['searchTerm'] = askAndReturnSearchTerm()
    contentTweets = robot.downloadTweets(content['searchTerm'])
<<<<<<< HEAD

    print('\nGerando Dataset...')
    dataSet = pd.DataFrame()
    
    print('\nCarregando tweets no Dataset...')
    dataSet['user_id'] = [tweet['user_id'] for tweet in contentTweets]
    dataSet['user'] = [tweet['user'] for tweet in contentTweets]
    dataSet['text'] = [tweet['text'] for tweet in contentTweets]
    dataSet['text_sanitized'] = [tweet['text_sanitized'] for tweet in contentTweets]
    dataSet['location'] = [tweet['location'] for tweet in contentTweets]
    dataSet['coordinates'] = [tweet['coordinates'] for tweet in contentTweets]
    dataSet['followers_count'] = [tweet['followers_count'] for tweet in contentTweets]
    dataSet['verified'] = [tweet['verified'] for tweet in contentTweets]
    dataSet['created_at'] = [tweet['created_at'] for tweet in contentTweets]
    tweets_place = []
    for tweet in contentTweets:
        if tweet['place']:
            tweets_place.append(tweet['place']['full_name'])
        else:
            tweets_place.append('null')
    dataSet['place'] = [i for i in tweets_place]
    
    print('\nAplicando Watson...')
    print('--SCORE--')
    dataSet['score'] = [sentimentWatson(tweet['text_sanitized'])['score'] for tweet in contentTweets]
    print('--SENTIMENTOS--')
    dataSet['sentiment'] = [sentimentWatson(tweet['text_sanitized'])['label'] for tweet in contentTweets]
    print('--KEYWORDS--')
    dataSet['keywords'] = [keywordsWatson(tweet['text_sanitized']) for tweet in contentTweets]

    print('\nExportando Dataset em CSV...')
    dataSet.to_csv('dataSet.csv', sep=';')

    print('\nDataset salvo com Sucesso!')
=======
    content['tweet'] = []

    for i in contentTweets:

        try:        
            data = {
                'user_id': i['user_id'],
                'user': i['user'],
                'TextOriginal': i['text'],
                'TextSanitized': i['text_sanitized'],
                'location': i['location'],
                'place': i['place'],
                'tweet_lon': i['tweet_lon'],
                'tweet_lat': i['tweet_lat'],
                'followers_count': i['followers_count'],
                'verified': i['verified'],
                'created_at': i['created_at'],
                'sentiment': sentimentWatson(i['text_sanitized']),
                'keywords': keywordsWatson(i['text_sanitized'])
            }
            
            content['tweet'].append(data)

            print('Aplicando análise de sentimentos com o Watson...,')

        except:
            print('Não foi possível aplicar o Watson!')
 
    print(content)
>>>>>>> 36d599ae7b7f83083f44dffdb1d9614d542f3b9b

def askAndReturnSearchTerm():
    """
    inserir termo para busca inclusive com operadores avançados de pesquisa do twitter (OR, AND, -, #, FROM, TO, @, SINCE, UNTIL)
    """
    return input('Digite o termo a ser pesquisado no Twitter: ') 


if __name__ == "__main__":
    main()