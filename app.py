import os

from flask import Flask, url_for, redirect
from  fast_search import make_request
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():

    name = os.environ.get('SEARCH_REPO', 'acse-7-2019-2020-assessment-acse')

    df = make_request(name, 1)
    i = 2
    while True:
        try:
            df = df.append(make_request(name, i))
            i += 1
        except:
            break

    df.insert(3, 'updated',
              (df.updated_at-df.created_at)>np.timedelta64(5, 'm'))

    df = df.iloc[df.name.str.lower().argsort()]

    print(df)
    

    return df.set_index('name').to_html()
