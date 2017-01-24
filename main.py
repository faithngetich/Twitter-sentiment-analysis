# Entry point of the application
from tweet import *

# Gets user twitter handle
twitter_handle = raw_input("Enter twitter handle:")

tweets = get_tweets(twitter_handle)
print(tweets)
