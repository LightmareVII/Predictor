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

posts = []
comments = {}

def runThis():
    wrapper = connectReddit()

    subReddit = ['Finance', 'Investing', 'worldnews', 'politics']
    for sub in subReddit:
        dataSUBS, dataCOMMENTS = wrapper.getSub(sub, 1)
        fields1 = ['id',
                   'title',
                   'selftext',
                   'subreddit',
                   'created',
                   'is_video',
                   'url',
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
                   'sorted_by']
        """
        fields2 = ['submissionID',
                   'id',
                   'body',
                   'author',
                   'votes',
                   'created',
                   'parent']
        """
        
        #do stuff with data
        for postkey in dataSUBS.keys():
            if postkey not in posts:
                posts.append(postkey) #list of all submissions by id only
                comments[postkey] = []
                with open('D:\Python Projects\Predictor\Subs.csv',
                          mode = 'a',
                          encoding = 'utf-8') as csv_file:
                    csv_writer = csv.DictWriter(csv_file,
                                                fieldnames = fields1,
                                                lineterminator = '\n')
                    csv_writer.writerow(dataSUBS[postkey])
                    csv_file.close()
                    
                for commentkey in dataCOMMENTS[postkey].keys():
                    if commentkey not in comments[postkey]:
                        comments[postkey].append(commentkey)
                        commentsList = [postkey]
                        [commentsList.append(x) for x in dataCOMMENTS[postkey][commentkey].values()]
                        with open('D:\Python Projects\Predictor\Comments.csv',
                                  mode = 'a',
                                  encoding = 'utf-8') as csv_file2:
                            csv_writer2 = csv.writer(csv_file2,
                                                     lineterminator = '\n')
                            csv_writer2.writerow(commentsList)
                            csv_file2.close()
                                                     

"""       
newlist = [data[x]['title'] for x in data.keys()] - newlist with all titles from data

SAME AS

newlist = []
for x in data.keys():
    newlist.append(data[x]['title'])

"""
"""
LEGACY
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
              'score']
    
    csv_writer = csv.DictWriter(csv_file,
                                fieldnames = fields,
                                lineterminator = '\n')
    csv_writer.writeheader()
    
    for x in dataSUBS:
        csv_writer.writerow(dataSUBS[x]) #submisisons with over 100 comments tended to line break and start a new record mid-export
    
    csv_file.close()
"""
