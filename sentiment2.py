##import nltk
##import ssl
##
##try:
##    _create_unverified_https_context = ssl._create_unverified_context
##except AttributeError:
##    pass
##else:
##    ssl._create_default_https_context = _create_unverified_https_context
##
##nltk.download()

import nltk
nltk.download('vader_lexicon')
nltk.download('tsla')

# first, we import the relevant modules from the NLTK library
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# next, we initialize VADER so we can use it within our Python script
sid = SentimentIntensityAnalyzer()

# the variable 'message_text' now contains the text we will analyze.
##message_text = '''Like you, I am getting very frustrated with this process. I am genuinely trying to be as reasonable as possible. I am not trying to "hold up" the deal at the last minute. I'm afraid that I am being asked to take a fairly large leap of faith after this company (I don't mean the two of you -- I mean Enron) has screwed me and the people who work for me.'''
message_text  = 'stocks'

print(message_text)

# Calling the polarity_scores method on sid and passing in the message_text outputs a dictionary with negative, neutral, positive, and compound scores for the input text
scores = sid.polarity_scores(message_text)

# Here we loop through the keys contained in scores (pos, neu, neg, and compound scores) and print the key-value pairs on the screen
for key in sorted(scores):
        print('{0}: {1}, '.format(key, scores[key]), end='')


##
##import nltk
##from nltk.tokenize import word_tokenize, RegexpTokenizer
##from nltk.sentiment.vader import SentimentIntensityAnalyzer
##import pandas as pd
##
##Analyzer = SentimentIntensityAnalyzer()
##
##sentence = 'enter your text to test'
##
##tokenized_sentence = nltk.word_tokenize(sentence)
##pos_word_list=[]
##neu_word_list=[]
##neg_word_list=[]
##
##for word in tokenized_sentence:
##    if (Analyzer.polarity_scores(word)['compound']) >= 0.1:
##        pos_word_list.append(word)
##    elif (Analyzer.polarity_scores(word)['compound']) <= -0.1:
##        neg_word_list.append(word)
##    else:
##        neu_word_list.append(word)                
##
##print('Positive:',pos_word_list)
##print('Neutral:',neu_word_list)
##print('Negative:',neg_word_list) 
##score = Analyzer.polarity_scores(sentence)
##print('\nScores:', score)
##
##sentence = 'stocks were volatile on Tuesday due to the recent calamities in the Chinese market'
##
##
