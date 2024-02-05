from flask import Flask, request, jsonify


app = Flask(__name__)

matches = [
    #turno pessoas moedas carta
    {
        "matche_id" : 1,
        "room_id" : 1,
        "player" : 1,
        "player_1_id" : 1,
        "player_2_id" : 2,
        "player_3_id" : 3,
        "player_4_id" : 4,
        "cheedar_1": 1,
        "cheedar_2": 1,
        "cheedar_3": 1,
        "cheedar_4": 1,
        "card_player" : 1
    }
]

@app.route("/matches/<int:id>", methods = ["PUT"])
def put_aluno(id):
     Update_match = request.get_json()

     for i, match in enumerate(matches):
        if id == match["id"]:
             matches[i].update(Update_match)
             return jsonify(matches)
            
        return jsonify({"erro":"partida nao encontrado"})
     
app.run(debug=True)