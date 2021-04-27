#!/usr/bin/env python

import tweepy
from datetime import datetime, timedelta
import os

# options
days_to_delete_after = 31

consumer_key = os.environ.get(TWITTER_API_KEY)
consumer_secret = os.environ.get(TWITTER_API_SECRET_KEY)
access_token = os.environ.get(ACCESS_TOKEN)
access_token_secret = os.environ.get(ACCESS_TOKEN_SECRET)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# set cutoff date, use utc to match twitter
cutoff_date = datetime.utcnow() - timedelta(days=days_to_delete_after)

timeline = tweepy.Cursor(api.user_timeline).items()
deletion_count = 0

for tweet in timeline:
	if tweet.created_at < cutoff_date:
		api.destroy_status(tweet.id)
		deletion_count += 1

print(f"{deletion_count} tweets happened before {cutoff_date.date()}, these have now been deleted")

favorites = tweepy.Cursor(api.favorites).items()
unlike_count = 0

for tweet in favorites:
	if tweet.created_at < cutoff_date:
		api.destroy_favorite(tweet.id)
		unlike_count += 1

print(f"{unlike_count} likes happened before {cutoff_date.date()}, these have now been unliked")
