import tweepy
from tweepy import OAuthHandler
 
consumer_key = 'eZOKy8akjnGcbRPoIWwCMSH58'
consumer_secret = 'O6fhokq5fFy1cR5hyc355hrZhsutorZAM4NJgPcBtaKZjQklcg'
access_token = '367243497-d9aJiNbWKokCdLRZ24tKUYBNRHxxlodn8S8szovV'
access_secret = 'gfOhHMWjC1tOvVYydEUHvxXZQU5uCaMTSFBE9VwFQI24X'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

for status in tweepy.Cursor(api.home_timeline).items(3):
    # Process a single status
    print(status.text)
