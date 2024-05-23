from flask import Blueprint, current_app
from controllers.controller_termo import get_termo, set_termo, del_termo, get_palavras, put_termo

bp_termo = Blueprint('bp_termo', __name__)

bp_termo.route("/termo", methods=["POST"])(set_termo)
bp_termo.route("/termo", methods = ["GET"])(get_palavras)
bp_termo.route('/termo/<int:termo_id>', methods=['GET'])(get_termo)
bp_termo.route("/termo/<int:id>", methods = ["PUT"])(put_termo)
bp_termo.route("/termo/<int:id>", methods = ["DELETE"])(del_termo)