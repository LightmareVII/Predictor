# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 21:50:28 2019

@author: Lightmare
"""

from wrapper import connectReddit

wrapper = connectReddit()

subReddit = ['finance']
posts = []
comments = {}

for sub in subReddit:
    data = wrapper.getSub(sub, 5)
    
    #do stuff with data
    for postkey in data.keys():
        posts.append(postkey)
        comments[postkey] = []
        
        for commentkey in data[postkey]['comments'].keys():
            comments[postkey].append(commentkey)
        
        
        
        
"""       
newlist = [data[x]['title'] for x in data.keys()] - newlist with all titles from data

SAME AS

newlist = []
for x in data.keys():
    newlist.append(data[x]['title'])

"""