"""
wrappers to make connections to various APIs
"""
import praw

class connectReddit(object):
    def __init__(self):
        self.CLIENT_ID = '_x2PTISsyViP3g'
        self.CLIENT_SECRET = 'syZ1LiodSb9RGXSGmZ7djaL8Apk'
        self.USER_AGENT = 'LanPredictor-BETA by /u/LanPredictor'
        self.REDDIT = praw.Reddit(client_id = self.CLIENT_ID,
                                  client_secret = self.CLIENT_SECRET,
                                  user_agent = self.USER_AGENT)
        
    def getReplies(self, Comment):
        pass #will need to step through and make nested dictionary of all comment replies
    
    def getComments(self, POST):
        self.RETURN_COMMENTS = {}
        
        self.SUBMISSION = self.REDDIT.submission(id = POST)
        for COMMENT in self.SUBMISSION.comments:
            self.RETURN_COMMENTS[COMMENT.id] = {'id' : COMMENT.id,
                                                'body' : COMMENT.body,
                                                'author' : COMMENT.author,
                                                'votes' : COMMENT.ups - COMMENT.downs,
                                                'created' : COMMENT.created_utc}
        return(self.RETURN_COMMENTS)
        
    def getSub(self, SUBREDDIT, POST_LIMIT):
        self.RESPONSE = {}
        
        for POST in self.REDDIT.subreddit(SUBREDDIT).hot(limit=POST_LIMIT):
            self.RESPONSE[POST.id] = {'id': POST.id,
                                   'title' : POST.title,
                                   'selftext': POST.selftext,
                                   'subreddit': POST.subreddit_name_prefixed,
                                   'created' : POST.created_utc,
                                   'is_video' : POST.is_video,
                                   'url' : POST.url,
                                   'authorID': POST.author_fullname,
                                   'author': POST.author,
                                   'votes': POST.ups - POST.downs,
                                   'num_comments': POST.num_comments,
                                   'comments' : self.getComments(POST)}
            
        #(self.responseList.append(x) for x in self.REDDIT.subreddit(SUBREDDIT).hot(limit=POST_LIMIT))
        return(self.RESPONSE)
        
    def getUser(self, USER):
        if isinstance(USER, str):
            pass
        elif isinstance(USER, list):
            pass
        


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