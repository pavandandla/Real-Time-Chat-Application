from flask import Blueprint, request, session, jsonify
from controllers.room_controller import create_room, store_message,list_rooms
from flask_socketio import emit, join_room, leave_room
from config.database import socketio
from models.all_models import Room,Message
from config.database import db


chat_bp = Blueprint('chat_bp', __name__)

@chat_bp.route('/create_room', methods=['POST'])
def create_room_route():
    return create_room()

@chat_bp.route('/get_rooms', methods=['GET'])
def get_room_route():
    return list_rooms()

# Event to handle user joining a room
@socketio.on('join')
def on_join(data):
    room_name = data['room']
    username = data['user'] 

    room = Room.query.filter_by(name=room_name).first()
    if room:
        join_room(room_name)
        
        # Fetch previous messages from the room
        messages = Message.query.filter_by(room_id=room.id).order_by(Message.timestamp.desc()).limit(10).all()
        messages = [{'user': msg.username, 'content': msg.content} for msg in messages[::-1]]

        # Emit previous messages to the user
        # emit('previous_messages', messages, room=room_name)
        emit('previous_messages', messages, to=request.sid)
        # Emit join message
        emit('message', {'user': username, 'content': f"{username} has entered the room. {room_name}"}, to=room_name)

# Event to handle user leaving a room
@socketio.on('leave')
def on_leave(data):
    room_name = data['room']
    username = data['user']
    leave_room(room_name)
    emit('message', {'user': username, 'content': f"{username} has left the room.{room_name}"}, to=room_name)

# Event to handle sending a message in a room
@socketio.on('send_message')
def handle_message(data):
    room_name = data['room']
    msg_content = data['message']
    username = data['user']
    
    room = Room.query.filter_by(name=room_name).first()
    if room:
        # Store the message in the database
        message = Message(content=msg_content, room_id=room.id, username=username)
        db.session.add(message)
        db.session.commit()

        emit('message', {'user': username, 'content': msg_content}, to=room_name)

