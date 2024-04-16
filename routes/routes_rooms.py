from flask import Blueprint
from controllers.controller_rooms import create_room, get_rooms, delete_room, put_room, get_rooms_by_id

bp_rooms = Blueprint('bp_rooms', __name__)

bp_rooms.route('/rooms', methods=['POST'])(create_room)
bp_rooms.route('/rooms', methods=['GET'])(get_rooms) 
bp_rooms.route('/rooms/<int:room_id>', methods=['DELETE'])(delete_room)
bp_rooms.route('/rooms/<int:id>', methods=['PUT'])(put_room)
bp_rooms.route('/rooms/<int:id>', methods=['GET'])(get_rooms_by_id)