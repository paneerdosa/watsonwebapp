"""
Flask application factory for the sentiment analysis web app.
"""

from flask import Flask
import sys

def create_app():
    """Create and configure the Flask application."""
    print("*** Creating Flask app...", file=sys.stderr)
    app = Flask(__name__)
    from . import routes
    app.register_blueprint(routes.bp)
    print("*** Flask app created successfully", file=sys.stderr)
    return app

# Create the application instance for Gunicorn
app = create_app()