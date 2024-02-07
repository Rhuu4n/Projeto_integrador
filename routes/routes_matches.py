from flask import Blueprint 
from controllers.controllers_partida import set_matches, get_matches, put_matches, get_matches_by_id

bp_matches = Blueprint('bp_matches', __name__)

app.route("/matches", methods=["POST"])(set_matches)
app.route("/matches", methods=["GET"])(get_matches)
app.route("/matches/<int:id>", methods=["PUT"])(put_matches)
app.route("/matches/<int:id>", methods=["DELETE"])(delete_matches)
app.route("/matches/<int:id>", methods=["GET"])(get_matches_by_id)