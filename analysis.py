# Add functionality to get sentiments
from watson_developer_cloud import AlchemyLanguageV1

def alchemy(words):
    print(words)
    alchemy_language = AlchemyLanguageV1(api_key='a7f5da4c25eeea912cee000a9fbe17860c24e819')
    # sentiment dictionry
    sentiment = alchemy_language.sentiment(text=words)
    sentiment_type = sentiment['docSentiment']['type']

    emotion = alchemy_language.emotion(text=words)
    anger = emotion['docEmotions']['anger']
    fear = emotion['docEmotions']['fear']
    joy = emotion['docEmotions']['joy']
    sadness = emotion['docEmotions']['sadness']
    disgust = emotion['docEmotions']['disgust']

    print('Your tweets are ', sentiment_type)
    print('Anger ==> ', anger)
    print('Fear ==> ', fear)
    print('Joy ==> ', joy)
    print('Sadness ==> ', sadness)
    print('Disgust ==> ', disgust)
