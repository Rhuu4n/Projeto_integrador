from flask import Flask, request, jsonify

from controllers.controllers_matches import set_matches, get_matches, put_matches, get_matches_by_id, delete_matches
from controllers.controller_rooms import create_room, get_rooms, delete_room, put_room

app = Flask(__name__)


app.register_blueprint(bp_users)

# Create, Read, Update do objeto partida
app.route("/matches", methods=["POST"])(set_matches)
app.route("/matches", methods=["GET"])(get_matches)
app.route("/matches/<int:id>", methods=["PUT"])(put_matches)
app.route("/matches/<int:id>", methods=["DELETE"])(delete_matches)
app.route("/matches/<int:id>", methods=["GET"])(get_matches_by_id)

# Create, Read, Update Das informações da sala
app.route('/create_room', methods=['POST'])(create_room) 
app.route('/create_room', methods=['GET'])(get_rooms) 
app.route('/delete_room/<int:room_id>', methods=['DELETE'])(delete_room)

app.run(debug=True)
