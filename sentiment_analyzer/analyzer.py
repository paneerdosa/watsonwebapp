"""
Sentiment analysis module using TextBlob.
Provides a function to analyze sentiment of text and return label and score.
"""

from textblob import TextBlob


def sentiment_analyzer(text):
    """
    Analyze sentiment of the given text using TextBlob.

    Args:
        text (str): The input text to analyze.

    Returns:
        dict: A dictionary with 'label' (positive/negative/neutral) and
              'score' (float between -1 and 1). If an error occurs,
              returns a dict with an 'error' key.
    """
    # Validate input
    if not isinstance(text, str):
        return {'error': 'Invalid input: text must be a string'}
    if not text.strip():
        return {'error': 'Text cannot be empty'}

    # Limit text length to avoid performance issues
    if len(text) > 5000:
        return {'error': 'Text too long (max 5000 characters)'}

    try:
        # Create a TextBlob object
        blob = TextBlob(text)

        # Get the polarity score (-1 to 1)
        sentiment_score = blob.sentiment.polarity

        # Handle case where score is None (should not happen, but just in case)
        if sentiment_score is None:
            return {'error': 'Sentiment analysis returned no result'}

        # Determine label based on score
        if sentiment_score > 0.05:
            label = 'positive'
        elif sentiment_score < -0.05:
            label = 'negative'
        else:
            label = 'neutral'

        # Return formatted result
        return {
            'label': label,
            'score': round(sentiment_score, 4)
        }
    except Exception as e:
        return {'error': f'Unexpected error during analysis: {str(e)}'}
