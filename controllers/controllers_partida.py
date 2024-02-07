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
          "usuario":"Hugo",
          "senha":"123",
          "e-mail":"rhuan123@rhuan123.com",
          "nascimento":"28/03/2003"
     }
]

id_content = {
    'last_matche_id' : 1
}

def set_matches(): #function
    
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

def get_matches():
    return jsonify (matches)

def put_matches(id):
     Update_match = request.get_json()

     for i, match in enumerate(matches):
        if id == match["matche_id"]:
             matches[i].update(Update_match)
             return jsonify(matches)
            
        return jsonify({"erro":"partida nao encontrado"})
     
def delete(id):

    for delete in matches:
        if delete['id'] == matches['id']:
            delete.remove(delete)
            return jsonify({"Apagada":"Partida Deletada"}), 200
        
    return({"error": "Partida Nao Encontrada"}), 404

def get_matches_by_id(id):
    for i, match in enumerate (matches):
        if id == match["id"]:
            return jsonify(match[i])
 
 
    return jsonify({"Erro":"Partida Nao Encontrada"}),404
