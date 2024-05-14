from factory import create_app
from flask_sqlalchemy import SQLAlchemy

socketio, app = create_app()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

if __name__ == "__main__":
    socketio.run(app, debug=True, host="0.0.0.0", port=3000, use_reloader=True, log_output=False)
