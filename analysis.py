# Add functionality to get sentiments
from watson_developer_cloud import AlchemyLanguageV1
from main import get_user_input

def alchemy(words):
    alchemy_language = AlchemyLanguageV1(api_key='a7f5da4c25eeea912cee000a9fbe17860c24e819')
    # sentiment dictionry
    if words is not None:
        sentiment = alchemy_language.sentiment(text=words)
        sentiment_type = sentiment['docSentiment']['type']

        emotion = alchemy_language.emotion(text=words)
        anger = emotion['docEmotions']['anger']
        fear = emotion['docEmotions']['fear']
        joy = emotion['docEmotions']['joy']
        sadness = emotion['docEmotions']['sadness']
        disgust = emotion['docEmotions']['disgust']

        from prettytable import PrettyTable
        print("")
        print("")
        sentiment_table = PrettyTable(["SENTIMENT"])
        sentiment_table.add_row([sentiment_type])
        print(sentiment_table)
        print("")
        print("")
        print("")

        alchemy_table = PrettyTable(["EMOTION", "VALUE"])
        alchemy_table.add_row(["Anger", anger])
        alchemy_table.add_row(["Fear", fear])
        alchemy_table.add_row(["Joy", joy])
        alchemy_table.add_row(["sadness", sadness])
        alchemy_table.add_row(["disgust", disgust])
        print(alchemy_table)
