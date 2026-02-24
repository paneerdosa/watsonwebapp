from flask import Blueprint, request, jsonify
from sentiment_analyzer.analyzer import sentiment_analyzer

bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET'])
def index():
    return jsonify({"message": "Sentiment Analysis API. Use POST /analyze with JSON {'text': 'your text'}"})

@bp.route('/analyze', methods=['POST'])
def analyze():
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
        return jsonify(result), 500
    return jsonify(result), 200