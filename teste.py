import json
import jsonpickle

import json
from pprint import pprint


with open('tweets.json') as data_file:
    data_item = json.load(data_file)
    
pprint(data_item)