from flask import Flask, request, jsonify

matches = [
   
    {
        "Jogador_ID" : 1,
        "id_sala" : 1,
        "Ordem" : 1,
        "Moedas" : 0,
        "Carta_1" : 1,
        "Carta_2" : 1,
        "Acao" : 1,
        "Afetado" : 1,
        "id_partida" : 1000
    }
]

def set_matches(): #function
    

    return jsonify(matches)



def get_matches():
    return jsonify (matches)



def put_matches(id):
     
    return jsonify({"Erro":"Partida Nao Encontrada"})


     
def delete_matches(id):

    return jsonify({"Erro": "Partida Nao Encontrada"}), 404



def get_matches_by_id(id):

    return jsonify({"Erro":"Partida Nao Encontrada"}),404


