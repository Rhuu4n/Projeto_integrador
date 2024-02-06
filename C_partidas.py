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

users = [
     {
          "id":1,
          "usuario":"Rhuan",
          "senha":"123",
          "e-mail":"rhuan123@rhuan123.com",
          "nascimento":"28/03/2003"
     },
    {
          "id":2,
          "usuario":"Rhuan",
          "senha":"123",
          "e-mail":"rhuan123@rhuan123.com",
          "nascimento":"28/03/2003"
     },
    {
          "id":3,
          "usuario":"Rhuan",
          "senha":"123",
          "e-mail":"rhuan123@rhuan123.com",
          "nascimento":"28/03/2003"
     },
    {
          "id":4,
          "usuario":"Rhuan",
          "senha":"123",
          "e-mail":"rhuan123@rhuan123.com",
          "nascimento":"28/03/2003"
     }
]

id_content = {
    'last_matche_id' : 1
}


@app.route("/matches", methods=["POST"]) # rota post
def set_students(): #function
    
    new_matche = request.get_json() # objeto retorna enviado pelo http
    id_content['last_matche_id'] += 1
    new_matche['matche_id'] = id_content['last_matche_id']
    new_matche['player'] = new_matche['player_1_id']
    
    players_foundeds = 0
    
    for user in users:
        if new_matche['player_1_id'] == user['id']:
            players_foundeds += 1
        if new_matche['player_2_id'] == user['id']:
            players_foundeds += 1
        if new_matche['player_3_id'] == user['id']:
            players_foundeds += 1
        if new_matche['player_4_id'] == user['id']:
            players_foundeds += 1
    
    if not players_foundeds == 4:
        return jsonify({"erro": players_foundeds})
  
    matches.append(new_matche)
    return jsonify(matches)

app.run(debug=True) 