# controllers/Room_controller.py
from flask import request, session, jsonify
from config.database import db
from models.all_models import Room, Message, User
from datetime import datetime

def create_room():
    data = request.json
    room_name = data.get('room_name')

    if Room.query.filter_by(name=room_name).first():
        return jsonify({'message': 'Room already exists'}), 400

    new_room = Room(name=room_name)
    db.session.add(new_room)
    db.session.commit()
    return jsonify({'message': 'Room created successfully'}), 201

def store_message(room_id, username, message_content):
    new_message = Message(room_id=room_id, username=username, content=message_content, timestamp=datetime.utcnow())
    db.session.add(new_message)
    db.session.commit()

def list_rooms():
    rooms = Room.query.all()
    return jsonify({"rooms": [room.name for room in rooms]})
