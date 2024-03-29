# Add functionality to get tweets

# python library that enables Python to communicate with Twitter  and use its API.
import tweepy
import json
# import progressbar
import time, sys
import re
from tqdm import tqdm
from stop_words import get_stop_words
# from nltk.corpus import stopwords
from string import punctuation

# generates stopwords
# customestopwords = set(stopwords.words('english') + list(punctuation))
customestopwords = get_stop_words('en')

from analysis import alchemy


# twitter access tokens (security keys from the twitter application)

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
    bar = progressbar.ProgressBar(widgets=['Fetching Tweets: ', progressbar.Bar(), ' (', progressbar.Timer(), ') ',], maxval=40)
    try:
        count = 0
        bar.start()
        for tweet in tweepy.Cursor(api.user_timeline, screen_name=twitter_handle).items(40):
            time.sleep(0.5)
            count += 1
            bar.update(count)
            tweets.append(tweet.text)
        bar.finish()
        with open("tweet.json","w") as file:
            json.dump(tweets, file, indent=4)
        words = tweets_to_words(tweets)

        return words
    except tweepy.TweepError as e:
        if e.response.status_code == 404:  # not found
            return None


def progress_bar():

    bar = progressbar.ProgressBar(widgets=[
        'Fetching Tweets: ',
        progressbar.Bar(),
        ' (', progressbar.Timer(), ') ',
    ])
    for i in bar(range(40)):
        time.sleep(0.5)


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
        if word not in customestopwords and len(word)>2:
            if not word.isdigit() and (not word.startswith('https')):
                if not any(char.isdigit() for char in word):
                    string_words.append(word.encode('utf-8').lower())
    return string_words
