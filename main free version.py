import tweepy
from textblob import TextBlob
import pandas as pd
import matplotlib.pyplot as plt
import tweepy.client

#setup auth
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
bearer_token = 'YOUR_BEARER_TOKEN'
access_token = 'YOUR_ACCESS_TOKEN'
access_secret = 'YOUR_ACCESS_SECRET'

#authenticating
client = tweepy.Client( 
    bearer_token=bearer_token,
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_secret)

#fetch tweets from X
def fetch_tweets(keyword , count):
    try:
        response = client.search_recent_tweets(query=keyword ,tweet_fields=['context_annotations', 'created_at'], max_results = min(count,100))
        tweets = response.data
        return tweets
    except Exception as e:
        print(f"Error fetching tweets: {e}")
        return None
    

#get sentiment func
def get_sentiment(tweet_text):
    analysis = TextBlob(tweet_text)
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity == 0:
        return "Neutral"
    else:
        return "Negative"

#main func    
if __name__ == "__main__":        
    keyword = input("enter keyword :")
    count = int(input("count :"))
    tweets = fetch_tweets(keyword,count)

    if tweets:
        tweets_data = []
        for tweet in tweets:
            sentiment = get_sentiment(tweet.text)
            print(f"Tweet: {tweet.text}")
            print(f"Sentiment: {sentiment}")
            print("-" * 50)
            tweets_data.append({'Tweet' : tweet.text , 'Sentiment' : sentiment})

        #visualization
        df = pd.DataFrame(tweets_data)

        sentiment_count = df['Sentiment'].value_counts()
        sentiment_count.plot( kind='bar', color = ['green','blue','red'])
        plt.title('Sentiment distribution')
        plt.xlabel('Sentiment')
        plt.ylabel('Frequncy')
        plt.show()

    else:
        print("No tweets found.")
