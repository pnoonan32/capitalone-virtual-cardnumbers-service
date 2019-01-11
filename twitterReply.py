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

phraseOne = "Hey, are you a student? We offer services created for students in mind. Feel free to DM us or visit https://bit.ly/2QEeuEe to learn more!"
phraseTwo = "Looking to learn more about our student services? Feel free to DM us or visit https://bit.ly/2QEeuEe to learn more!"

# debug
# user = api.me()
# print(user.name)    

def replyTweet():

    current = 2
    counter = 0
    search= ("student loans", "c1HackathonTest")

    numberofTweets = 1

    for tweet in tweepy.Cursor(api.search, search).items(numberofTweets):
        current = counter / 2
        
        tweetId = tweet.user.id
        username = tweet.user.screen_name
        u = api.get_user(username)
        if current < 1:      
            try:
                api.update_status("@"+username+" "+ phraseOne, in_reply_to_status_id = tweetId, in_reply_to_user_id = u.id)
                print("Replied. - 1")
                counter = 2
            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                break

        elif current > 1:
            try:
                api.update_status("@"+username+" "+ phraseTwo, in_reply_to_status_id = tweetId, in_reply_to_user_id = u.id)
                print("Replied. - 2")
                counter = 0
            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                break
replyTweet()
