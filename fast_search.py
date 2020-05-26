import os
import sys
import json
from urllib import request, error

import pandas as pd
import numpy as np

token = os.environ['GITTOKEN']
org = os.environ.get('SEARCH_ORG', 'acse-2019')
variables = os.environ.get('SEARCH_VARIABLES',
                           'name:created_at:updated_at').split(':')

def make_request(name, page):
    base_url = "https://api.github.com"
    endpoint = f'/search/repositories?q={name}+in:name+org:{org}&page={page}' 
    req = request.Request(base_url+endpoint)
    req.add_header('content-type', 'application/json')
    req.add_header('Authorization', f'token {token}')

    resp = request.urlopen(req)
    resp = json.load(resp)

    return pd.read_json(json.dumps(resp['items']))[variables]



if __name__ == '__main__':

    name = sys.argv[1]
    
    df = make_request(name, 1)
    i = 2
    while True:
        try:
            df = df.append(make_request(name, i))
            i += 1
        except:
            break

    df.insert(3, 'updated', (df.updated_at-df.created_at)>np.timedelta64(5, 'm'))

    print(df)

    df.to_csv(sys.argv[2])
