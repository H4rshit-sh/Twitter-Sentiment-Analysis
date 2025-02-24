import tweepy
from textblob import TextBlob
import pandas as pd
import matplotlib.pyplot as plt

#setup auth
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
bearer_token = 'YOUR_BEARER_TOKEN'
access_token = 'YOUR_ACCESS_TOKEN'
access_secret = 'YOUR_ACCESS_SECRET'

#authenticating 
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)
api = tweepy.API(auth , wait_on_rate_limit= True)

#get sentiment func
def get_sentiment(tweet):
        analysis = TextBlob(tweet.text)
        if analysis.sentiment.polarity > 0:
            return "Positive"
        elif analysis.sentiment.polarity == 0:
            return 'Neutral'
        else:
            return 'Negative'

#fetching tweeets
keyword = input("enter keyword :")
key_count = int(input("count :"))
public_tweets = api.search_tweets(keyword, count = key_count)

for tweet in public_tweets:
    sentiment = get_sentiment(tweet.text)
    print(f"Tweet: {tweet.text}")
    print(f"Sentiment: {sentiment}")
    print("-" * 50)

df = pd.DataFrame({'Tweet': [tweet.text for tweet in public_tweets], 'Sentiment': sentiment})

sentiment_count = df['Sentiment'].value_counts()
sentiment_count.plot( kind='bar', color = ['green','blue','red'])
plt.title =('Sentiment distribution')
plt.xlabel = ('Sentiment')
plt.ylabel= ('Frequncy')
plt.show()
