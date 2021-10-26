import tweepy
from datetime import date
import pandas as pd

path = 'C:/Users/alcob/Desktop/Projects/Tweety'

with open(path + '/' + 'keys.txt') as f:
    keys = f.readlines()
keys = list(map(lambda x: x.split(":")[1].split("\n")[0],keys))        

auth = tweepy.OAuthHandler(keys[0], keys[1])
auth.set_access_token(keys[2], keys[3])
api = tweepy.API(auth)

date = date.today()

keywords = ['Facebook', 'Apple', 'Amazon', 'Netflix', 'Google']

number_of_tweets = 400
tweets = []
likes = []
time = []
category = []

for word in keywords:
    for i in tweepy.Cursor(api.search, q = word, tweet_mode = "extended").items(number_of_tweets):
        tweets.append(i.full_text)
        likes.append(i.favorite_count)
        time.append(i.created_at)
        category.append(word)

df = pd.DataFrame({'tweets':tweets,'likes':likes,'time':time, 'category':category})

filename = 'tweets_'+str(date)+'.csv'
df.to_csv(path + "/data/" +filename)