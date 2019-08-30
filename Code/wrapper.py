"""
wrappers to make connections to various APIs
"""
#add initial database check
import praw
from praw.models import MoreComments
import time

#may have gone a little self happy - discovered it in my last project and it helped me immensely

class connectReddit():
    def __init__(self):
        self.CLIENT_ID = '_x2PTISsyViP3g'
        self.CLIENT_SECRET = 'syZ1LiodSb9RGXSGmZ7djaL8Apk'
        self.USER_AGENT = 'LanPredictor-BETA by /u/LanPredictor'
        self.REDDIT = praw.Reddit(client_id = self.CLIENT_ID,
                                  client_secret = self.CLIENT_SECRET,
                                  user_agent = self.USER_AGENT)
        self.index = 1
        
    
    def getComments(self, POST):
        RETURN_COMMENTS = {}
        
        SUBMISSION = self.REDDIT.submission(id = POST)
        for COMMENT in SUBMISSION.comments.list():
            if isinstance(COMMENT, MoreComments):
                continue
            else:
                RETURN_COMMENTS[COMMENT.id] = {'id' : COMMENT.id,
                                               'body' : COMMENT.body,
                                               'author' : COMMENT.author,
                                               'votes' : COMMENT.ups - COMMENT.downs,
                                               'created' : COMMENT.created_utc,
                                               'parent': COMMENT.parent_id.split('_')[-1]}
        return(RETURN_COMMENTS)
    
    
    def combSub(self, POST, SORT):
        submissions = {}
        comments = {}
        for submission in POST:
            submissions[submission.id] = {'id': submission.id,
                                          'title' : submission.title,
                                          'selftext': submission.selftext,
                                          'subreddit': submission.subreddit_name_prefixed,
                                          'created' : submission.created_utc,
                                          'is_video' : submission.is_video,
                                          'url' : submission.url,
                                          'author': submission.author,
                                          'votes': submission.ups - submission.downs,
                                          'vote_ratio' : submission.upvote_ratio,
                                          'num_comments': submission.num_comments,
                                          'media' : submission.media,
                                          'stickied' : submission.stickied,
                                          'subscribers' : submission.subreddit_subscribers,
                                          'num_crossposts' : submission.num_crossposts,
                                          'pinned' : submission.pinned,
                                          'awards' : submission.total_awards_received,
                                          'score' : submission.score,
                                          'sorted_by': SORT}
            
            comments[submission.id] = self.getComments(submission)
        return(submissions, comments)
            
            
    def getSub(self, SUBREDDIT, POST_LIMIT):
        print('{:^25}'.format(SUBREDDIT))
        print('{:^25}'.format(POST_LIMIT))
        start = time.time()
        RESPONSE_SUB = {}
        RESPONSE_COMMENT = {}
        
        sortList = ['hot','new','controversial','top','rising']
        
        POST_LIST = [self.REDDIT.subreddit(SUBREDDIT).hot(limit = POST_LIMIT),
                     self.REDDIT.subreddit(SUBREDDIT).new(limit = POST_LIMIT),
                     self.REDDIT.subreddit(SUBREDDIT).controversial(limit = POST_LIMIT),
                     self.REDDIT.subreddit(SUBREDDIT).top(limit = POST_LIMIT),
                     self.REDDIT.subreddit(SUBREDDIT).rising(limit = POST_LIMIT)]
        sortIndex = 0
        for sortItem in POST_LIST:
            print('{:<25}'.format(sortList[sortIndex]))
            sortedSubs, sortedComments = self.combSub(sortItem, sortList[sortIndex])
            RESPONSE_SUB.update(sortedSubs)
            RESPONSE_COMMENT.update(sortedComments)
            sortIndex += 1
            
        print('{:>30}'.format('%s seconds elapsed' % round((time.time() - start), 2)))
        return(RESPONSE_SUB, RESPONSE_COMMENT)
###############################################################################
#                                                                             #
#                                                                             #
#                               NOT YET IMPEMENTED                            #
#                                                                             #
#                                                                             #
###############################################################################

class connectTwitter(object):
    def __init__():
        pass

class connectYahoo(object):
    def __init__():
        pass
        
class connectMarkets(object):       #one per market
    def __init__():
        pass

test = connectReddit()