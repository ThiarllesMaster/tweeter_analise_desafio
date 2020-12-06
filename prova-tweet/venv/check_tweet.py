import tweepy
import credentials
import graph
from textblob import TextBlob

consumer_key = credentials.consumer_key
consumer_secret = credentials.consumer_secret
access_token = credentials.access_token
access_token_secret = credentials.access_token_secret

#Connection to tweeter
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

name = input("Inform the tweet which you want to obtain information:")
tweets = api.search(name)

tweet_positive = 0
tweet_negative = 0
tweet_neutral =  0
total_tweets = 0

for tweet in tweets:
    phrase = TextBlob(tweet.text)
    if (phrase.sentiment.polarity == 0):
        tweet_neutral = tweet_neutral + 1
        total_tweets = total_tweets + 1
        print(tweet.text)
    elif (phrase.sentiment.polarity < 0):
        tweet_negative = tweet_negative + 1
        total_tweets = total_tweets + 1
        print(tweet.text)
    elif (phrase.sentiment.polarity > 0):
        tweet_positive = tweet_positive +1
        total_tweets = total_tweets + 1
        print(tweet.text)

def calculate_percentage(quantity, total_tweets):
    if (quantity == 0):
        return  0
    elif (quantity > 0):
      return 100 * float(quantity) / float(total_tweets)

tweet_positive = calculate_percentage(tweet_positive, total_tweets)
tweet_negative = calculate_percentage(tweet_negative, total_tweets)
tweet_neutral = calculate_percentage(tweet_neutral,   total_tweets)

graph.drawGraph(tweet_positive, tweet_negative, tweet_neutral)
