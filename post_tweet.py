import tweepy

CONSUMER_KEY = 'jh3MD5yOdWcwz9DCRCEefxhWT'
CONSUMER_SECRET = 'PmW6K1hFRHk5uqVNWYp12hCgA6mEv1gQsq4IxpAl9CD086mBjk'
ACCESS_KEY = '1137839206783422464-GwpljDLKLiJ6Ee5V3iO7GyzqjyphZ4'
ACCESS_SECRET = 'BOPi63pJAGCKtbcGIaNvQU1kYvg6QxWWhSlIWp05lOsXF'

def post_tweet( tweet_content ) :

    auth = tweepy.OAuthHandler( CONSUMER_KEY, CONSUMER_SECRET )
    auth.set_access_token( ACCESS_KEY, ACCESS_SECRET )

    tweet = "You:\nMe, woke: " + tweet_content

    api = tweepy.API( auth )
    api.update_status( tweet )
