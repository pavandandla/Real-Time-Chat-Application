# controllers/Chat_controller.py
from flask import request, jsonify, session
from flask_socketio import emit, join_room, leave_room
from config.database import db,socketio
from models.all_models import User, Room, Message
from app import socketio


# Event to handle sending a message in a room
@socketio.on('send_message')
def handle_message(data):
    room_name = data['room']
    msg_content = data['message']
    username=data['user']
    room = Room.query.filter_by(name=room_name).first()
    if room:
        message = Message(content=msg_content, room_id=room.id, username=username)
        db.session.add(message)
        db.session.commit()
        emit('message', {'user':username , 'msg': msg_content}, room=room_name)




