# from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.corpus import stopwords
from string import punctuation
from tweet import *

# generates stopwords
customestopwords = set(stopwords.words('english') + list(punctuation))

# returns word without stopwords
def non_stopwords(tweets):
    words = []
    if tweets is None:
        print "That user does not exist."
        return None
    for word in tweets:
        if word not in customestopwords:
            words.append(word)
    return words


# gets the frequency of words in tweets and displays it in a preety tab
def most_freq_words(words):
    from prettytable import PrettyTable

    word_freq = {}
    for word in words:
        try:
            if word_freq[word]:
                word_freq[word] += 1
        except KeyError:
            word_freq[word] = 1

    words_table = PrettyTable(["WORD", "FREQ"])
    count = 0
    for word in sorted(word_freq, key=word_freq.get, reverse=True):
        if count != 20:
            words_table.add_row([word,word_freq[word]])
            count += 1
        else:
            return words_table
