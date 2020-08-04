from flask import Flask,render_template,request,jsonify
import tweepy
from textblob import TextBlob


#---------------------------------------------------------------------------

consumer_key = '3kRte46jNNaeu5BfAlh2gASxQ'
consumer_secret = 'khfh6W7hSx5gFYQPsjYPzUUyI31liRjtb7KZPWqvlv39kO1uR3'

access_token = '1160650024973303809-x9xDUqAIvufNfi70MJeXgqWZjPrHpr'
access_token_secret = 'uRzL1GqZE1bAUJM4QcErQpjGFW291eCcVHS8DAGzWDRqT'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#-------------------------------------------------------------------------

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/search",methods=["POST"])
def search():
    search_tweet = request.form.get("search_query")
    
    t = []
    tweets = api.search(search_tweet, tweet_mode='extended')
    for tweet in tweets:
        polarity = TextBlob(tweet.full_text).sentiment.polarity
        subjectivity = TextBlob(tweet.full_text).sentiment.subjectivity
        t.append([tweet.full_text,polarity,subjectivity])
        # t.append(tweet.full_text)

    return jsonify({"success":True,"tweets":t})

app.run()
