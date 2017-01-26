# Add functionality to get tweets

# python library that enables Python to communicate with Twitter  and use its API.
import tweepy
import json
import re
from tqdm import tqdm
from stop_words import get_stop_words

from analysis import alchemy

# get english stopwords
stop_words = get_stop_words('en')

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
    # api_response = api.user_timeline(screen_name = twitter_handle, count = 200)
    # tweets = parse_tweets(api_response)
    # return tweets
    tweets = []
    for tweet in tqdm(tweepy.Cursor(api.user_timeline, screen_name=twitter_handle).items(20)):
        tweets.append(tweet.text)
    with open("tweet.json","w") as file:
        json.dump(tweets, file, indent=4)
    words = tweets_to_words(tweets)

    return words

# returns words of the tweet fetched by the api response and stores them in a list
def parse_tweets(api_response):
    tweets = []

    for tweet in api_response:
        tweets.append(tweet.text)
    words = tweets_to_words(tweets)
    return words


def tweets_to_words(tweets):
    # cleans up tweets words from regular expression
    words = []
    for tweet in tweets:
        # w removes unicode
        words += re.compile('\w+').findall(tweet)
    return clean_text(words)


def clean_text(words):
    # converts unicode characters to string
    string_words = [] # empty list of words
    for word in words:
        if word[0].isdigit():
            continue
        elif word in stop_words:
            continue
        string_words.append(word.encode('utf-8').lower())
    return string_words
