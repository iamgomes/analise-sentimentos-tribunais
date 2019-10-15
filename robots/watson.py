# -*- Coding: UTF-8 -*-
#coding: utf-8

import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, SentimentOptions, KeywordsOptions
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from decouple import config
import pandas as pd


def sentimentKeywordsWatson(file):

    df = pd.read_csv(file, sep=';')
    df['score'] = None
    df['sentiment'] = None
    df['keywords'] = None

    authenticator = IAMAuthenticator(config('apikey'))
    natural_language_understanding = NaturalLanguageUnderstandingV1(
        version='2019-07-12',
        authenticator=authenticator
    )

    natural_language_understanding.set_service_url(config('url'))

    for i in range(len(df)):
        print('Aplicando IA... buscando keywords de {}'.format(i))
        tweet = df.loc[i, 'text_sanitized']

        try:
            response = natural_language_understanding.analyze(
                text=tweet,
                features=Features(keywords=KeywordsOptions(limit=1))).get_result()    

            doc_ini = json.dumps(response)
            doc_fim = json.loads(doc_ini) 

            keywords = []
    
            [keywords.append(i['text'].lower()) for i in doc_fim['keywords'][0:]]   

            df.loc[i, 'keywords'] = keywords

        except:
            None

    for i in range(len(df)):
        print('Aplicando IA... calculando score e sentimento de {}'.format(i))
        text_sanitized = df.loc[i, 'text_sanitized']

        try:
            response = natural_language_understanding.analyze(
                text=text_sanitized,
                features=Features(sentiment=SentimentOptions())).get_result()

            doc_ini = json.dumps(response)
            doc_fim = json.loads(doc_ini)

            df.loc[i, 'score'] = doc_fim['sentiment']['document']['score']
            df.loc[i, 'sentiment'] = doc_fim['sentiment']['document']['label']

        except:
            None

    
    file_name = 'dataSet_final.csv'
    df.to_csv(file_name, sep=';')

    print('Arquivo {} gerado com sucesso!'.format(file_name))