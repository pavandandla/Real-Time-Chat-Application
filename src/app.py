from flask import Flask
from config.config import Config
from config.database import db, socketio
from routes.chat_bp import chat_bp
from routes.user_bp import user_bp
from models.all_models import User, Room, Message

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
socketio.init_app(app)

# Register blueprints
app.register_blueprint(chat_bp)
app.register_blueprint(user_bp)

with app.app_context():
    db.create_all()  # Ensure database tables are created

if __name__ == '__main__':
    socketio.run(app, debug=True)