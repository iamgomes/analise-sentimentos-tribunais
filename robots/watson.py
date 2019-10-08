# -*- coding: utf8 -*-
import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, SentimentOptions, KeywordsOptions
from decouple import config
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def sentimentWatson(content):

    authenticator = IAMAuthenticator(config('apikey'))
    natural_language_understanding = NaturalLanguageUnderstandingV1(
        version='2019-07-12',
        authenticator=authenticator
    )

    natural_language_understanding.set_service_url(config('url'))
    
    response = natural_language_understanding.analyze(
        text=content,
        features=Features(sentiment=SentimentOptions())).get_result()    

    doc_ini = json.dumps(response)
    doc_fim = json.loads(doc_ini)

    return doc_fim['sentiment']['document']


def keywordsWatson(content):

    authenticator = IAMAuthenticator(config('apikey'))
    natural_language_understanding = NaturalLanguageUnderstandingV1(
        version='2019-07-12',
        authenticator=authenticator
    )

    natural_language_understanding.set_service_url(config('url'))
    
    response = natural_language_understanding.analyze(
        text=content,
        features=Features(keywords=KeywordsOptions(limit=3))).get_result()    

    doc_ini = json.dumps(response)
    doc_fim = json.loads(doc_ini)

    return doc_fim['keywords']