from flask import Flask
from twitter import analize_latest_tweet, preprocess_latest_tweet

app = Flask(__name__)

@app.route('/')
def index():
  return 'I am online and ready, Mr. Stark\n'

@app.route('/preprocess_latest/<user>')
def preprocess_latest(user):
  return preprocess_latest_tweet(user)
  
@app.route('/user_sentiment/<user>')
def user_sentiment(user):
  return analize_latest_tweet(user)