"""
Flask application factory for the sentiment analysis web app.
"""

from flask import Flask


def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)
    from . import routes
    app.register_blueprint(routes.bp)
    return app


# Create the application instance for Gunicorn
app = create_app()