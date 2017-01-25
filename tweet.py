# Add functionality to get tweets

# python library that enables Python to communicate with Twitter  and use its API.
import tweepy

# twitter access tokens (security keys from the twitter application)
access_token = "3228931192-dgwDS0IabNwy3ujynR8BMq0k9Mky6dp3qErmydr"
access_token_secret = "sM067uSqM5XLu3gR6d2FxAfahxhxvBuxMuMnm2YqJjy9C"
consumer_key = "VHmz0kLyncU4mV2Idre5VQKyR"
consumer_secret = "XeT1YP657uPacDMPcAbMv94AwzaclZcJLF1J29xTeOzgvJGWam"

# twitter OAuth authentication
# Into OAuthHandler instance, we pass our consumer token and secret
# access token is the key for opening the Twitter API treasure box.
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
    words = tweets_to_words(tweets)
    return words


def tweets_to_words(tweets):
    # converts tweets to words
    words = []
    for tweet in tweets:
        words += tweet.title().split()
    return unicode_to_string(words)


def unicode_to_string(words):
    # converts unicode characters to string
    string_words = []
    for word in words:
        string_words.append(word.encode('utf-8').lower())
    return string_words
