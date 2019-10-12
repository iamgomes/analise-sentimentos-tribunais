# -*- Coding: UTF-8 -*-
#coding: utf-8

import robots.twitter as robot
import robots.geocode as geo
from robots.watson import sentimentWatson, keywordsWatson
import pandas as pd

def main():
    # cria dicionário de dados e sua estrutura
    content = {}

    content['searchTerm'] = askAndReturnSearchTerm()
    contentTweets = robot.downloadTweets(content['searchTerm'])

    print('\nGerando Dataset...')
    dataSet = pd.DataFrame()
    
    print('\nCarregando tweets no Dataset...')
    dataSet['user_id'] = [tweet['user_id'] for tweet in contentTweets]
    dataSet['user'] = [tweet['user'] for tweet in contentTweets]
    dataSet['text'] = [tweet['text'] for tweet in contentTweets]
    dataSet['text_sanitized'] = [tweet['text_sanitized'] for tweet in contentTweets]
    dataSet['followers_count'] = [tweet['followers_count'] for tweet in contentTweets]
    dataSet['verified'] = [tweet['verified'] for tweet in contentTweets]
    dataSet['created_at'] = [tweet['created_at'] for tweet in contentTweets]
    dataSet['coordinates'] = [tweet['coordinates'] for tweet in contentTweets]
    dataSet['location'] = [tweet['location'] for tweet in contentTweets]
    dataSet['place'] = [tweet['place'] for tweet in contentTweets]
    dataSet['lat'] = [geo.coordinates(tweet['location'])['lat'] for tweet in contentTweets]
    dataSet['lng'] = [geo.coordinates(tweet['location'])['lng'] for tweet in contentTweets]

    print('\nAplicando Watson...')
    print('--SCORE--')
    #dataSet['score'] = [sentimentWatson(tweet['text_sanitized'])['score'] for tweet in contentTweets]
    print('--SENTIMENTOS--')
    #dataSet['sentiment'] = [sentimentWatson(tweet['text_sanitized'])['label'] for tweet in contentTweets]
    print('--KEYWORDS--')
    #dataSet['keywords'] = [keywordsWatson(tweet['text_sanitized']) for tweet in contentTweets]

    print('\nExportando Dataset em CSV...')
    dataSet.to_csv('dataSet.csv', sep=';')

    print('\nDataset salvo com Sucesso!')


def askAndReturnSearchTerm():
    """
    inserir termo para busca inclusive com operadores avançados de pesquisa do twitter (OR, AND, -, #, FROM, TO, @, SINCE, UNTIL)
    """
    return input('Digite o termo a ser pesquisado no Twitter: ') 


if __name__ == "__main__":
    main()