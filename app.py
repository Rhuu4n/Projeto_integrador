from flask import Flask, request, jsonify
from controllers.controllers_users import get_users, set_users, del_users
from controllers.controllets_partida import set_matches, get_matches, put_matches

app = Flask(__name__)

# Create, Read e Delete do objeto users
app.route("/users", methods=["POST"])(set_users)
app.route("/users", methods = ["GET"])(get_users)
app.route("/users/<int:id>", methods = ["DELETE"])(del_users)
@app.route('/players/<int:player_id>', methods=['GET'])(get_player)

# Create, Read, Update do objeto partida
app.route("/matches", methods=["POST"])(set_matches)
app.route("/matches", methods=["GET"])(get_matches)
app.route("/matches/<int:id>", methods=["PUT"])(get_matches)

app.run(debug=True)
