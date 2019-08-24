# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 18:00:23 2019

@author: Lightmare

Purpose: Historial Data
"""

#https://api.pushshift.io/reddit/{}/search/

import requests
import time

now = int(time.time())

endpoint = 'https://api.pushshift.io/reddit/submission/search?'
myparams = {'subreddit' : 'Finance,Invest',
             'before' : now,
             'size' : '1000'}


req = requests.get(endpoint, params = myparams)
myjson = req.json()

test = myjson['data']

#myList = [[x['id'], x['selftext'], x['score']] for x in test]

mylist = []
for x in test:
    try:
        mylist.append([x['id'],
                      x['selftext'],
                      x['score']])
    except:
        print(x)
