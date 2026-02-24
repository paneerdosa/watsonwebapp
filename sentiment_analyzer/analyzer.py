from textblob import TextBlob

def sentiment_analyzer(text):
    if not isinstance(text, str):
        return {'error': 'Invalid input: text must be a string'}
    if not text.strip():
        return {'error': 'Text cannot be empty'}
    if len(text) > 5000:
        return {'error': 'Text too long (max 5000 characters)'}
    try:
        blob = TextBlob(text)
        score = blob.sentiment.polarity
        if score is None:
            return {'error': 'Sentiment analysis returned no result'}
        if score > 0.05:
            label = 'positive'
        elif score < -0.05:
            label = 'negative'
        else:
            label = 'neutral'
        return {'label': label, 'score': round(score, 4)}
    except Exception as e:
        return {'error': f'Unexpected error: {str(e)}'}