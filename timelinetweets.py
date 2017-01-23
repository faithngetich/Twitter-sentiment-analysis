import tweepy

access_token = "3228931192-dgwDS0IabNwy3ujynR8BMq0k9Mky6dp3qErmydr"
access_token_secret = "sM067uSqM5XLu3gR6d2FxAfahxhxvBuxMuMnm2YqJjy9C"
consumer_key = "VHmz0kLyncU4mV2Idre5VQKyR"
consumer_secret = "XeT1YP657uPacDMPcAbMv94AwzaclZcJLF1J29xTeOzgvJGWam"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text
