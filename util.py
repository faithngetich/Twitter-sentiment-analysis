def most_freq_words(words):
    word_freq = {}
    for word in words:
        if word not in word_freq:
            word_freq[word] = words.count(word)
    return word_freq

def display_word_freq(word_dict):
    print("word                    frequency")
    for k, v in sorted(word_dict.items(), key=lambda x: x[1], reverse=True):
        print("{0}  |  {1}".format(k, v))
