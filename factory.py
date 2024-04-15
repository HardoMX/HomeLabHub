from flask import Flask
from blueprints.dashboard import dash_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(dash_bp)

    return app
