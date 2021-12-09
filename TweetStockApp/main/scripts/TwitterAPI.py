import tweepy
from tweepy import API
from tweepy import Cursor
from tweepy import OAuthHandler
from django.conf import settings


class Twitter():

    def authenticate(self):
        auth = tweepy.OAuthHandler(settings.API_KEY, settings.API_KEY_SECRET)
        auth.set_access_token(settings.ACCESS_TOKEN,
                              settings.ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth, wait_on_rate_limit=True)
        return api

    def generate_twitter_data(self, username):
        api = self.authenticate()
        max_tweets = 50
        posts = []
        for tweet in tweepy.Cursor(api.user_timeline, screen_name=username, tweet_mode="extended", count=50, include_rts=False).items(max_tweets):
            posts.append(tweet)

        return posts
