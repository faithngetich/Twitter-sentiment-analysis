# Entry point of the application

# gets everything in the tweet, util and analysis file.
from tweet import *
from util import *
from analysis import *

# import the the util file

# Gets user twitter handle
twitter_handle = raw_input("Enter twitter handle:")

# gets tweets from the specified handle
tweets = get_tweets(twitter_handle)

# remove stopwords from tweets
tweets_without_stopwords = non_stopwords(tweets)

# analyse tweets
alchemy(' '.join(tweets_without_stopwords))

# returns the frequency of words used
word_freq = most_freq_words(tweets)

# display the frequency of a word
display_word_freq(word_freq)
