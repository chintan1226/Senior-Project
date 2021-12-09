from datetime import datetime
import re
import numpy as np
import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')


class Analysis():

    # TODO: Try different cleaning?
    def clean_text(self, text):
        text = re.sub(r'@[A-Za-z0-9]+', '', text)
        text = re.sub(r'#', '', text)
        text = re.sub(r'RT[\s]+', '', text)
        text = re.sub(r'http\S+|www.\S+', '', text)
        return text

    def get_analysis(self, tweet):
        analyzer = SentimentIntensityAnalyzer()
        vs = analyzer.polarity_scores(tweet)
        if vs['compound'] > 0:
            return "Positive"
        elif vs['compound'] < 0:
            return "Negative"
        else:
            return "Neutral"

    def get_polarity(self, tweet):
        analyzer = SentimentIntensityAnalyzer()
        vs = analyzer.polarity_scores(tweet)
        return ("Negative = " + str(vs["neg"]) + ",\nNeutral = " + str(vs["neu"]) + ",\nPositive = " + str(vs["pos"]) + ",\nCompound = " + str(vs["compound"]))

    def generate_analysis(self, posts):
        df = pd.DataFrame(
            [tweet.full_text for tweet in posts], columns=['Tweet'])

        df['Date'] = np.array(
            [datetime.strftime(tweet.created_at, '%B %d, %Y') for tweet in posts])

        df['Likes'] = np.array([tweet.favorite_count for tweet in posts])
        df['Retweets'] = np.array([tweet.retweet_count for tweet in posts])

        df['Tweet'] = df['Tweet'].apply(self.clean_text)
        df = df[df['Tweet'] != '']

        # Create columns for Analysis and Polarity
        df['Analysis'] = df['Tweet'].apply(self.get_analysis)
        df['Polarity'] = df['Tweet'].apply(self.get_polarity)

        return df
