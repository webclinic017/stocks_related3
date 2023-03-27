import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import twitter_samples 
 
nltk.download('twitter_samples')
nltk.download('vader_lexicon')
 
# get 5000 posivie and negative tweets
all_positive_tweets = twitter_samples.strings('positive_tweets.json')
all_negative_tweets = twitter_samples.strings('negative_tweets.json')
 
analyzer = SentimentIntensityAnalyzer()

analyzer.polarity_scores(all_positive_tweets[100])
analyzer.polarity_scores(all_negative_tweets[20])

my_labels = [1]*len(all_positive_tweets)
negative_labels = [0]*len(all_negative_tweets)
my_labels.extend(negative_labels)
 
all_positive_tweets.extend(all_negative_tweets)
 
df = pd.DataFrame({'tweets' : all_positive_tweets, 
                   'my_labels' : my_labels})
 
print(df) 
