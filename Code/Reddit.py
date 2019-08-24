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
import csv


wrapper = connectReddit()

subReddit = ['all']
posts = []
comments = {}

for sub in subReddit:
    data = wrapper.getSub(sub, None)
    
    #do stuff with data
    for postkey in data.keys():
        posts.append(postkey) #list of all submissions by id only
        comments[postkey] = []
        print(postkey,',', len(data[postkey]['comments']))
        
        for commentkey in data[postkey]['comments'].keys():
            comments[postkey].append(commentkey) #list of all comments by comment key only
                                                 #should also save parent key.  Idk if submission can be recorded.  that would be ideal
                                                 #also not sure if you plan on trying to follow conversations to gather info or take each one as a single data point
"""       
newlist = [data[x]['title'] for x in data.keys()] - newlist with all titles from data

SAME AS

newlist = []
for x in data.keys():
    newlist.append(data[x]['title'])

"""

with open('D:\Python Projects\Predictor\TestData.csv',
           mode='w',
           encoding = 'utf-8') as csv_file:
    
    fields = ['id',
              'title',
              'selftext',
              'subreddit',
              'created',
              'is_video',
              'url',
              'authorID',
              'author',
              'votes',
              'vote_ratio',
              'num_comments',
              'media',
              'stickied',
              'subscribers',
              'num_crossposts',
              'pinned',
              'awards',
              'score',
              'comments']
    
    csv_writer = csv.DictWriter(csv_file,
                                fieldnames = fields,
                                lineterminator = '\n')
    csv_writer.writeheader()
    #csv_writer.writerow((k, v.encode('utf-8')) for k, v in data.items()) #this didn't work any better
    
    for x in data:
        csv_writer.writerow(data[x]) #submisisons with over 100 comments tended to line break and start a new record mid-export
    
    csv_file.close()
    