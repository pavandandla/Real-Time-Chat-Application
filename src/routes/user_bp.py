
from flask import Blueprint
from controllers.user_controller import register, login, logout

user_bp = Blueprint('user_bp', __name__)

user_bp.route('/', methods=['GET', 'POST'])(register)
user_bp.route('/login', methods=['GET', 'POST'])(login)
user_bp.route('/logout')(logout)
