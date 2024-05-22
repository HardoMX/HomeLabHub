from flask import Flask
from blueprints.dashboard import dash_bp
from blueprints.cms import cms_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(dash_bp)
    app.register_blueprint(cms_bp)

    return app
