from flask import Flask,jsonify
from controllers.controller_rooms import get_rooms

app = Flask(__name__)

app.route("/rooms", methods=["GET"])(get_rooms)

app.run(debug=True)
