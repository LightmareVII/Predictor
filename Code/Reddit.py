# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 21:50:28 2019

@author: Lightmare
"""
"""
SQL query to pull all submissions and comment IDs.

run script -> compare gathered submissions to list of IDs.  any that don't exist yet, add to the database.

compare recursive list of gathered comments to existing in DB.  any that don't exist, append to comments 
field, using submission to put it in the right spot.

Below structures will store all submission IDs in a list.
Below structure will store all comment IDs in a dict with their submission as the key for identification.
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