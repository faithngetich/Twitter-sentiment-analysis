# Entry point of the application
from tweet import *
from util import *

# import the the util file

# Gets user twitter handle
twitter_handle = raw_input("Enter twitter handle:")

tweets = get_tweets(twitter_handle)

word_freq = most_freq_words(tweets)

display_word_freq(word_freq)
