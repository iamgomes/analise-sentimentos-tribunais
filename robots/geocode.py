# -*- Coding: UTF-8 -*-
#coding: utf-8

import requests
from decouple import config


def coordinates(address, api_key=config('api_key')):
    
    url = config('url_google')

    params = {
        'address' : address.encode('ascii', 'xmlcharrefreplace'),
        'sensor' : 'false'
    }

    if api_key:
        params['key'] = api_key

    response = requests.get(url, params=params)
    coord = response.json()

    if coord['status'] == 'OVER_QUERY_LIMIT':
        raise RuntimeError(coord['error_message'])

    if coord['status'] == 'OK':
        return {
            'lat': coord['results'][0]['geometry']['location']['lat'],
            'lng': coord['results'][0]['geometry']['location']['lng'],
        }
    else:
        return {
            'lat': '',
            'lng': '',
            }