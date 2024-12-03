"""from models.all_models import User, ChatRoom
from config.database import db
from werkzeug.security import generate_password_hash, check_password_hash

def register_user(data):
    username = data.get('username')
    password = data.get('password')
    if User.query.filter_by(username=username).first():
        return {"status": "failed", "message": "User already exists"}, 400  # Use failed status

    new_user = User(username=username, password=generate_password_hash(password))
    db.session.add(new_user)
    db.session.commit()
    return {"status": "success", "message": "User registered successfully"}, 201

def login_user(data):
    username = data.get('username')
    password = data.get('password')
    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password, password):
        return {"status": "failed", "message": "Invalid credentials"}, 401

    return {"status": "success", "message": "Login successful"}, 200

def create_chat_room(data):
    room_name = data['room_name']
    
    if ChatRoom.query.filter_by(name=room_name).first():
        return {"status": "failed", "message": "Room already exists"}, 400
    
    new_room = ChatRoom(name=room_name)
    db.session.add(new_room)
    db.session.commit()
    
    return {"status": "success", "message": f"Room '{room_name}' created successfully."}, 201 """
