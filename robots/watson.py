# -*- coding: utf8 -*-
import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, RelationsOptions, SentimentOptions, KeywordsOptions, MetadataOptions, EmotionOptions
from decouple import config

def sentimentWatson(content):
    natural_language_understanding = NaturalLanguageUnderstandingV1(
        version='2019-07-12',
        iam_apikey=config('apikey'),
        url=config('url')
    )

    response = natural_language_understanding.analyze(
        text=content,
        features=Features(sentiment=SentimentOptions())).get_result()    

    doc_ini = json.dumps(response)
    doc_fim = json.loads(doc_ini)

    return doc_fim['sentiment']['document']