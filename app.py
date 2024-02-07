from flask import Flask, request, jsonify

from controllers.controllers_users import get_users, set_users, del_users, get_user, put_user
from controllers.controllers_partida import set_matches, get_matches, put_matches, get_matches_by_id,delete_matches
from controllers.controller_rooms import create_room, get_rooms, delete_room, put_room

app = Flask(__name__)

# Create, Read e Delete do objeto users
app.route("/users", methods=["POST"])(set_users)
app.route("/users", methods = ["GET"])(get_users)
app.route("/users/<int:id>", methods = ["DELETE"])(del_users)
app.route("/users/<int:id>", methods = ["PUT"])(put_user)
app.route('/users/<int:user_id>', methods=['GET'])(get_user)

# Create, Read, Update do objeto partida
app.route("/matches", methods=["POST"])(set_matches)
app.route("/matches", methods=["GET"])(get_matches)
app.route("/matches/<int:id>", methods=["PUT"])(put_matches)
app.route("/matches/<int:id>", methods=["DELETE"])(delete_matches)
app.route("/matches/<int:id>", methods=["GET"])(get_matches_by_id)

# Create, Read, Update Das informações da sala
app.route('/create_room', methods=['POST'])(create_room) 
app.route("/rooms", methods=["GET"])(get_rooms)
app.route('/create_room', methods=['GET'])(get_rooms) 
app.route('/delete_room/<int:room_id>', methods=['DELETE'])(delete_room)
app.route("/rooms/<int:id>", methods = ["PUT"])(put_room)

app.run(debug=True)
