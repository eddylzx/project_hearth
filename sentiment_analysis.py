from textblob import TextBlob

def get_sentiment(text):
    # Create TextBlob object of text
    analysis = TextBlob(text)
    # Return sentiment from analysis object. Could also return subjectivity
    return analysis.sentiment.polarity

print(get_sentiment("oh my god that is not good"))