from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.corpus import stopwords
from string import punctuation
from tweet import *

# generates stopwords
customestopwords = set(stopwords.words('english') + list(punctuation))

# returns word without stopwords
def non_stopwords(tweets):
    words = []
    for word in tweets:
        if word not in customestopwords:
            words.append(word)
    return words


# gets the frequency of words in tweets
def most_freq_words(words):
    word_freq = {}
    for word in words:
        try:
            if word_freq[word]:
                word_freq[word] += 1
        except KeyError:
            word_freq[word] = 1
    return word_freq

# displays word frequency
def display_word_freq(word_dict):
    print("word                    frequency")
    # This will sort the dictionary values of each tweet within the dictionary from largest to smallest
    for k, v in sorted(word_dict.items(), key=lambda x: x[1], reverse=True):
        print("{0}  |  {1}".format(k, v))
