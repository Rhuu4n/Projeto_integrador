from flask import Flask, request, jsonify

matches = [
    #turno pessoas moedas carta
    {
        "id" : 1,
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

app = Flask(__name__)

@app.route("/matches")
def get_matches_by_id():
    return jsonify (matches)

app.run(debug=True)