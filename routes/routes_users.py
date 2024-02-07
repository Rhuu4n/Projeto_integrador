from flask import Blueprint 
from controllers.controllers_users import get_users, set_users, del_users, get_user, put_user

bp_users = Blueprint('bp_users', __name__)

bp_users.route("/users", methods=["POST"])(set_users)
bp_users.route("/users", methods = ["GET"])(get_users)
bp_users.route("/users/<int:id>", methods = ["DELETE"])(del_users)
bp_users.route("/users/<int:id>", methods = ["PUT"])(put_user)
bp_users.route('/users/<int:user_id>', methods=['GET'])(get_user)
