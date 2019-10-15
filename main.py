# -*- Coding: UTF-8 -*-
#coding: utf-8

import robots.twitter as robot
import robots.geocode as geo
from robots.watson import sentimentKeywordsWatson
import pandas as pd
import numpy as np

def main():
    # cria dicionário de dados e sua estrutura
    content = {}

    content['searchTerm'] = askAndReturnSearchTerm()
    contentTweets = robot.downloadTweets(content['searchTerm'])

    print('\nGerando Dataset...')
    dataSet = pd.DataFrame()
    
    print('\nCarregando tweets no Dataset...')
    dataSet['user_id'] = np.array([tweet['user_id'] for tweet in contentTweets])
    dataSet['user'] = np.array([tweet['user'] for tweet in contentTweets])
    dataSet['text'] = np.array([tweet['text'] for tweet in contentTweets])
    dataSet['text_sanitized'] = np.array([tweet['text_sanitized'] for tweet in contentTweets])
    dataSet['followers_count'] = np.array([tweet['followers_count'] for tweet in contentTweets])
    dataSet['verified'] = np.array([tweet['verified'] for tweet in contentTweets])
    dataSet['created_at'] = np.array([tweet['created_at'] for tweet in contentTweets])
    dataSet['coordinates'] = np.array([tweet['coordinates'] for tweet in contentTweets])
    dataSet['location'] = np.array([tweet['location'] for tweet in contentTweets])
    dataSet['place'] = np.array([tweet['place'] for tweet in contentTweets])
    dataSet['source'] = np.array([tweet['source'] for tweet in contentTweets])

    dataSet.to_csv('tweets.csv', sep=';')

    print('\nBuscando latitude e longitude...')
    geo.coordinates('tweets.csv')

    print('\nAplicando Watson...')
    sentimentKeywordsWatson('tweets_kml.csv.csv')

    print('\nExportando Dataset em CSV...')

    print('\nDataset salvo com Sucesso!')


def askAndReturnSearchTerm():
    """
    inserir termo para busca inclusive com operadores avançados de pesquisa do twitter (OR, AND, -, #, FROM, TO, @, SINCE, UNTIL)
    """
    return input('Digite o termo a ser pesquisado no Twitter: ') 


if __name__ == "__main__":
    main()