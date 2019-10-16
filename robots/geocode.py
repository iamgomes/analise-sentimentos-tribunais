# -*- Coding: UTF-8 -*-
#coding: utf-8

import googlemaps
from decouple import config
import pandas as pd


def coordinates(file):

    df = pd.read_csv(file, sep=';')
    df['lat'] = None
    df['lng'] = None

    gmaps_key = googlemaps.Client(key=config('api_key'))

    for i in range(len(df)):
        print('Buscando latitude e longitude de {}'.format(i))
        geocode_result = gmaps_key.geocode(df.loc[i, 'location'])
        try:
            lat = geocode_result[0]['geometry']['location']['lat']
            lng = geocode_result[0]['geometry']['location']['lng']
            df.loc[i, 'lat'] = lat
            df.loc[i, 'lng'] = lng
        except:
            lat = None
            lng = None

    file_name = 'tweets_kml.csv'
    df.to_csv(file_name, sep=';')

    print('Arquivo {} gerado com sucesso!'.format(file_name))