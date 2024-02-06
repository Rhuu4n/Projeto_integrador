from flask import Flask,jsonify
from controllers.controller_rooms import get_rooms

app = Flask(__name__)

app.route("/rooms", methods=["GET"])(get_rooms)


@app.route("/rooms/<int:id>", methods= ["GET"])
def get_rooms_by_id(id):
    for i, get_rooms in enumerate (get_rooms):
        if id == get_rooms_by_id ["id"]:
            return jsonify(get_rooms[i])


    return jsonify({"Sala Não Encontrada"})

app.run(debug=True)
