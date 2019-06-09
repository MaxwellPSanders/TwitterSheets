import tweepy

CONSUMER_KEY = 'XXXX'
CONSUMER_SECRET = 'XXXX'
ACCESS_KEY = 'XXXX-XXXX'
ACCESS_SECRET = 'XXXX'

def post_tweet( tweet_you, tweet_me ) :

    auth = tweepy.OAuthHandler( CONSUMER_KEY, CONSUMER_SECRET )
    auth.set_access_token( ACCESS_KEY, ACCESS_SECRET )

    tweet = "You: " + tweet_you + "\nMe, woke: " + tweet_me
    if len( tweet ) < 280 :
        api = tweepy.API( auth )
        api.update_status( tweet )
