# DON'T FORGET 

import tweepy

consumer_key = 'ata1zzvdbVukkcmwZUQD69RJR'
consumer_secret =   'ZmFkQHH36aHmzMk1QcgANIejEaDdL7MxaJJZJd7ptS9eIc79qr'
access_token =  '2564020243-sG0CpQDH7plmp630omZZu1o8VyOYJCrtOzRma5z'
access_token_secret =   'QmW1L5QhA3Abf7qu5dt6lt2TO9hkQEPu1JrbKqrLfB7Un'

# set auth variables
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# create a new api
api = tweepy.API(auth)

phrase = "wow! peep our site!"
phraseTwo = "it happens :/"


# debug
# user = api.me()
# print(user.name)

def waitTime():
    time.sleep(90)  # wait 90 seconds
    

def replyTweet():
    search= ("testing #WhateverYouWantYourHashtagToBe")

    numberofTweets = 1

    for tweet in tweepy.Cursor(api.search, search).items(numberofTweets):
        try:
            tweetId = tweet.user.id
            username = tweet.user.screen_name
            u = api.get_user(username)
            
            api.update_status("@"+username+" "+phrase, in_reply_to_status_id = tweetId, in_reply_to_user_id = u.id)
            print("Replied.")
            #time.sleep(90)
            waitTime()            
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break
        



replyTweet()
