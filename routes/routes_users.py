from flask import Blueprint, current_app
from controllers.controllers_users import get_users, set_users, del_users, get_user, put_user, login_user, get_token

bp_users = Blueprint('bp_users', __name__)

bp_users.route("/cadastro", methods=["POST"])(set_users)
bp_users.route("/users", methods = ["GET"])(get_users)
bp_users.route("/users/<int:id>", methods = ["DELETE"])(del_users)
bp_users.route("/users/<int:id>", methods = ["PUT"])(put_user)
bp_users.route('/users/<int:user_id>', methods=['GET'])(get_user)
bp_users.route("/login", methods=["POST"])(login_user)
bp_users.route("/token", methods=["get"])(get_token)