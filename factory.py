from flask import Flask
from blueprints.dashboard import dash_bp
from flask_socketio import SocketIO

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "secret!"

    app.register_blueprint(dash_bp)
    socketio = SocketIO(app)

    return socketio, app
