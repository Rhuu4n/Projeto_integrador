from flask import Flask,jsonify
from controllers.controller_rooms import get_rooms,rooms

app = Flask(__name__)

app.route("/rooms", methods=["GET"])(get_rooms)


@app.route("/rooms/<int:id>", methods= ["GET"])
def get_rooms_by_id(id):
    for i, room in enumerate (rooms):
        if id == room["id"]:
            return jsonify(rooms[i])

    return jsonify({"Erro":"Sala Nao Encontrada"}),404




app.run(debug=True)


