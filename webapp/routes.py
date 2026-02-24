"""
Route definitions for the sentiment analysis API.
"""

from flask import Blueprint, request, jsonify
from sentiment_analyzer.analyzer import sentiment_analyzer

bp = Blueprint('main', __name__)


@bp.route('/', methods=['GET'])
def index():
    """Root endpoint returning API usage information."""
    return jsonify({
        "message": "Sentiment Analysis API. Use POST /analyze with JSON {'text': 'your text'}"
    })


@bp.route('/analyze', methods=['POST'])
def analyze():
    """
    Analyze sentiment of provided text.

    Expects JSON: {"text": "some text"}
    Returns JSON with sentiment label and score, or error.
    """
    # Check if request is JSON
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 415

    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({"error": "Missing 'text' field in JSON"}), 400

    text = data['text'].strip()
    if not text:
        return jsonify({"error": "Text cannot be empty"}), 400

    result = sentiment_analyzer(text)
    if 'error' in result:
        # Return error with 500 status
        return jsonify(result), 500
    return jsonify(result), 200
