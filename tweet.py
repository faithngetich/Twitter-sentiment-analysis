# Add functionality to get tweets

import tweepy

# twitter access tokens
access_token = "3228931192-dgwDS0IabNwy3ujynR8BMq0k9Mky6dp3qErmydr"
access_token_secret = "sM067uSqM5XLu3gR6d2FxAfahxhxvBuxMuMnm2YqJjy9C"
consumer_key = "VHmz0kLyncU4mV2Idre5VQKyR"
consumer_secret = "XeT1YP657uPacDMPcAbMv94AwzaclZcJLF1J29xTeOzgvJGWam"

# twitter OAuth authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# get an instance of the twitter api
api = tweepy.API(auth)


def get_tweets(twitter_handle):

    # return 200 tweets belonging to the given twitter handle
    api_response = api.user_timeline(screen_name = twitter_handle, count = 200)
    tweets = parse_tweets(api_response)
    return tweets

def parse_tweets(api_response):
    tweets = []
    for tweet in api_response:
        tweets.append(tweet.text)
    return tweets
