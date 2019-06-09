import tweepy

CONSUMER_KEY = 'XXXX'
CONSUMER_SECRET = 'XXXX'
ACCESS_KEY = 'XXXX-XXXX'
ACCESS_SECRET = 'XXXX'

def post_tweet( tweet_content ) :

    auth = tweepy.OAuthHandler( CONSUMER_KEY, CONSUMER_SECRET )
    auth.set_access_token( ACCESS_KEY, ACCESS_SECRET )

    tweet = "You:\nMe, woke: " + tweet_content

    api = tweepy.API( auth )
    api.update_status( tweet )
