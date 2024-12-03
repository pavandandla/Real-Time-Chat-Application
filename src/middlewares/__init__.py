from flask import request, Response, g
from functools import wraps
import jwt
import os
import logging

def decode_jwt(token):
    try:
        token = token.split(" ")[1]  # Split the token in 'Bearer <token>' format
        return jwt.decode(token, str(os.getenv('SECRET_KEY')), algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        logging.error("Token has expired")
        return {'error': 'Token has expired'}
    except jwt.InvalidTokenError:
        logging.error("Invalid token")
        return {'error': 'Invalid token'}

def authenticate_admin(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get('Authorization')

        if not auth_header:
            logging.warning("Missing Authorization header")
            return Response(
                response='{"message": "Unauthorized - Missing Authorization header"}',
                status=401
            )

        user_info = decode_jwt(auth_header)

        if 'error' in user_info:
            return Response(
                response=f'{{"message": "Unauthorized - {user_info["error"]}"}}',
                status=401
            )

        if 'role' not in user_info or user_info['role'] != 'admin':
            logging.warning("User is not authorized")
            return Response(
                response='{"message": "Unauthorized - User is not authorized"}',
                status=403
            )

        g.user_info = user_info  # Set user information in global `g`
        
        return func(*args, **kwargs)  # Proceed to the actual function

    return wrapper