import tweepy
from textblob import TextBlob
import credentials
import graph

# inicial variables
tweet_positive = 0
tweet_negative = 0
tweet_neutral = 0

auth = tweepy.OAuthHandler(credentials.consumer_key, credentials.consumer_secret)
auth.set_access_token(credentials.access_token, credentials.access_token_secret)
api = tweepy.API(auth)

name = input("Inform the tweet which you want to obtain information:")
number_tweets = int(input("How many tweets do you want verify?"))

tweets = tweepy.Cursor(api.search, q=name).items(number_tweets)
print(tweets)

for tweet in tweets:
    analyze = TextBlob(tweet.text)
    if (analyze.sentiment.polarity == 0.0):
        tweet_neutral = tweet_neutral + 1
    elif (analyze.sentiment.polarity < 0.00):
        tweet_negative = tweet_negative + 1
    elif (analyze.sentiment.polarity > 0.00):
        print("Tweet Positive")


def calculate_percentage(quantity, total_tweets):
    return 100 * float(quantity) / float(total_tweets)


tweet_positive = calculate_percentage(number_tweets, tweet_positive)
tweet_negative = calculate_percentage(number_tweets, tweet_negative)
tweet_neutral = calculate_percentage(number_tweets, tweet_neutral)

graph.drawGraph(tweet_positive, tweet_negative, tweet_neutral)
