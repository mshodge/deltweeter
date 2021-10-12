#!/usr/bin/env python

# standard libs
from datetime import datetime, timedelta, timezone
import os

# third-party libs
import tweepy

# variables
days_to_delete_after = 31

# constants
deletion_count = 0  # do not change
unlike_count = 0  # do not change

# env variables of Twitter API tokens taken from GitHub Secrets
consumer_key = os.environ['TWITTER_API_KEY']
consumer_secret = os.environ['TWITTER_API_SECRET_KEY']
access_token = os.environ['ACCESS_TOKEN']
access_token_secret = os.environ['ACCESS_TOKEN_SECRET']

# Twitter Auth
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# set cutoff date, use utc to match twitter
cutoff_date = datetime.now() - timedelta(days=days_to_delete_after)

# Get users timeline (tweets)
timeline = tweepy.Cursor(api.user_timeline).items()

# Deletes tweets
for tweet in timeline:
	if tweet.created_at < cutoff_date:
		api.destroy_status(tweet.id)
		deletion_count += 1
print(f"{deletion_count} tweets happened before {cutoff_date.date()}, these have now been deleted")

# Get users favourites
favorites = tweepy.Cursor(api.favorites).items()

for tweet in favorites:
	if tweet.created_at < cutoff_date:
		api.destroy_favorite(tweet.id)
		unlike_count += 1
print(f"{unlike_count} likes happened before {cutoff_date.date()}, these have now been unliked")
