"""
Minimal test app for debugging deployment.
"""

from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return {"message": "Hello World! The app is working."}

    @app.route('/test')
    def test():
        return {"status": "ok"}

    return app

app = create_app()