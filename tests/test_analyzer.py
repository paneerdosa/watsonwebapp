"""
Unit tests for the sentiment analyzer module.
"""

import unittest
from sentiment_analyzer.analyzer import sentiment_analyzer


class TestSentimentAnalyzer(unittest.TestCase):
    """Test cases for sentiment_analyzer function."""

    def test_positive_sentiment(self):
        """Test that positive text returns positive label and score > 0."""
        result = sentiment_analyzer("I love this product! It's amazing.")
        self.assertEqual(result['label'], 'positive')
        self.assertGreater(result['score'], 0)

    def test_negative_sentiment(self):
        """Test that negative text returns negative label and score < 0."""
        result = sentiment_analyzer("This is terrible. I hate it.")
        self.assertEqual(result['label'], 'negative')
        self.assertLess(result['score'], 0)

    def test_neutral_sentiment(self):
        """Test that neutral text returns neutral label and score near 0."""
        result = sentiment_analyzer("It is a desk.")
        self.assertEqual(result['label'], 'neutral')
        self.assertAlmostEqual(result['score'], 0, delta=0.1)

    def test_empty_text(self):
        """Test that empty string returns error."""
        result = sentiment_analyzer("")
        self.assertIn('error', result)

    def test_non_string_input(self):
        """Test that non-string input returns error."""
        result = sentiment_analyzer(123)
        self.assertIn('error', result)


if __name__ == '__main__':
    unittest.main()
