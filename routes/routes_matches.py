from flask import Blueprint 
from controllers.controllers_partida import set_matches, get_matches, put_matches, get_matches_by_id, delete_matches

bp_matches = Blueprint('bp_matches', __name__)

bp_matches.route("/matches", methods=["POST"])(set_matches)
bp_matches.route("/matches", methods=["GET"])(get_matches)
bp_matches.route("/matches/<int:id>", methods=["PUT"])(put_matches)
bp_matches.route("/matches/<int:id>", methods=["DELETE"])(delete_matches)
bp_matches.route("/matches/<int:id>", methods=["GET"])(get_matches_by_id)