from flask import Flask, request, jsonify
from routes.routes_users import bp_users
from routes.routes_matches import bp_matches
from routes.routes_rooms import bp_rooms

app = Flask(__name__)


app.register_blueprint(bp_users)
app.register_blueprint(bp_matches)
app.register_blueprint(bp_rooms)

app.run(debug=True)
