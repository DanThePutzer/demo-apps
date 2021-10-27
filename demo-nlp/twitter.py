import tweepy
import re
import string

import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')

from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Initializing tweepy
auth = tweepy.OAuthHandler("XXVbjMseDmvqck8Ky6lRVGbRG", "zdKwiM83GYEmPC93TJWnhx4natvFzhzXougQ5uMsYijbMzGGaw")
api = tweepy.API(auth)

# Function to preprocess tweet for sentiment analysis
def preprocess_tweet_text(tweet):
    tweet.lower()
    # Remove urls
    tweet = re.sub(r"http\S+|www\S+|https\S+", '', tweet, flags=re.MULTILINE)
    # Remove user @ references and '#' from tweet
    tweet = re.sub(r'\@\w+|\#','', tweet)
    # Remove punctuations
    tweet = tweet.translate(str.maketrans('', '', string.punctuation))
    # Remove stopwords
    tweet_tokens = word_tokenize(tweet)
    filtered_words = [w for w in tweet_tokens if not w in stopwords.words()]
    print(filtered_words)
    
    return " ".join(filtered_words)

# Function to perform a simple sentiment analysis on latest user tweet
def analize_latest_tweet(user):
    # Get last tweet by user
    lastTweet = api.user_timeline(user, count=1)[0]
    # Process tweet using proper function
    processedTweet = preprocess_tweet_text(lastTweet.text)
    # Initialize and execute simple sentiment analysis
    sid = SentimentIntensityAnalyzer()
    ratings = sid.polarity_scores(processedTweet)
    # Return result dictionary
    return {
        "user": api.get_user(user).screen_name,
        "tweet_text": lastTweet.text,
        "sentiment": ratings
    }

# Function to fetch and preprocess latest tweet
def preprocess_latest_tweet(user):
    # Get last tweet by user
    lastTweet = api.user_timeline(user, count=1)[0]
    # Process tweet using proper function
    processedTweet = preprocess_tweet_text(lastTweet.text)
    # Return result dictionary
    return {
        "user": api.get_user(user).screen_name,
        "original_tweet": lastTweet.text,
        "preprocessed_tweet": processedTweet
    }