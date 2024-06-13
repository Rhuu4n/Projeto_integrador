from flask import Blueprint 
from controllers.controllers_matches import set_matches, get_matches, put_matches, get_matches_by_id, delete_matches, get_matches_by_room_id

bp_matches = Blueprint('bp_matches', __name__)

# put this sippet ahead of all your bluprints
# blueprint can also be app~~
@bp_matches.after_request 
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    # Other headers can be added here if needed
    return response

# put this sippet ahead of all your bluprints
# blueprint can also be app~~
@bp_matches.after_request 
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    # Other headers can be added here if needed
    return response

bp_matches.route("/matches", methods=["POST"])(set_matches)
bp_matches.route("/matches", methods=["GET"])(get_matches)
bp_matches.route("/matches/<int:id>", methods=["PUT"])(put_matches)
bp_matches.route("/matches/<int:id>", methods=["DELETE"])(delete_matches)
bp_matches.route("/matches/<int:id>", methods=["GET"])(get_matches_by_id)
bp_matches.route("/matches/room", methods=["GET"])(get_matches_by_room_id)