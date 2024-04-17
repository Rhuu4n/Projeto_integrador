from flask import Flask, request, jsonify
from models.models_rooms import Salas
from app import db

def create_room():
    new_room = request.get_json()

    crt_room = Salas.from_json(new_room)
    db.session.add(crt_room)
    db.session.commit()
        
    return jsonify(crt_room.to_json()), 201    
    
def get_rooms():
    rooms =  Salas.query.all()

    return [c.to_json() for c in rooms]

def delete_room (room_id):
    
    del_room = db.get_or_404(Salas, id)
    db.session.delete(del_room)
    db.session.commit()

    return jsonify({"Excluido":"Evento foi deletado com sucesso"}), 200


def put_room(id):

    put_room = request.get_json()

    p_room = db.get_or_404(Salas, id)

    p_room.jogadorAtual = put_room.get("jogadorAtual")
    p_room.estadoSala = put_room.get("estadoSala")
    p_room.numeroJogadores = put_room.get("numeroJogadores")
    
    db.session.commit()

    return jsonify(p_room.to_json()), 201

def get_rooms_by_id(id):
    p_room = db.get_or_404(Salas, id)
    return jsonify(p_room.to_json()), 201
