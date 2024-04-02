from flask import Flask, request, jsonify
from models.models_rooms import Salas
from app import db

rooms = [
    {
        "id":555,
        "status_room":0,
        "player_1_id": 1,
        "player_2_id": 2,
        "player_3_id": 3,
        "player_4_id": 4
    }
]

def create_room():
    new_room = request.get_json()

    room = Salas.from_json(new_room)
    db.session.add(room)
    db.session.commit()
        
    return jsonify(room.to_json()), 201    
    
def get_rooms():
    return jsonify(rooms)


def delete_room (room_id):

    for room in rooms:
        if room['id'] == room_id:
            rooms.remove(room)
            return jsonify({'mensagem': 'sala deletada com sucesso'}), 200
        
    return({'error': 'Sala não encontrada'}), 404

def put_room(id):
     update_room = request.get_json()

     for i, room in enumerate(rooms):
        if id == room["id"]:
             rooms[i].update(update_room)
             return jsonify(room)
            
     return jsonify({"erro":"user nao encontrado"}), 404

def get_rooms_by_id(id):
    for i, room in enumerate (rooms):
        if id == room["id"]:
            return jsonify(rooms[i])
 
    return jsonify({"Erro":"Sala Nao Encontrada"}),404