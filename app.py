from flask import Flask, request, jsonify
from routes.routes_users import bp_users
from routes.routes_matches import bp_matches



from controllers.controller_rooms import create_room, get_rooms, delete_room, put_room

app = Flask(__name__)


app.register_blueprint(bp_users)
app.register_blueprint(bp_matches)



app.route('/create_room', methods=['POST'])(create_room)
app.route('/create_room', methods=['GET'])(get_rooms) 
app.route('/delete_room/<int:room_id>', methods=['DELETE'])(delete_room)

app.run(debug=True)
