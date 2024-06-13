from flask import Flask, request, jsonify
from models.models_matches import Matches
from app import db

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

    new_match = request.get_json()
    match = Matches.from_json(new_match)
    db.session.add(match)
    db.session.commit()
    
    return jsonify(match.to_json()), 201

def get_matches():
    matches = Matches.query.all()
    return jsonify ([match.to_json() for match in matches])



def put_matches(id):

    put_match = request.get_json()
    a_match = db.get_or_404(Matches, id)
    a_match.Ordem = put_match.get('Ordem')
    a_match.Carta_1 = put_match.get('Carta_1')
    a_match.Carta_2 = put_match.get('Carta_2')
    a_match.Acao = put_match.get('Acao')
    a_match.Afetado = put_match.get('Afetado')

    db.session.commit()

    return jsonify(a_match.to_json()), 201


     
def delete_matches(id):

    a_match = db.get_or_404(Matches, id)
    db.session.delete(a_match)
    db.session.commit()

    return jsonify(a_match.to_json())



def get_matches_by_id(id):
    matches = db.session.query(Matches).filter_by(id_partida = id).first()
    if matches is None:
        return jsonify({'error': 'Partida não encontrada'}), 404
    return jsonify(matches.to_json()), 200

def get_matches_by_room_id():
    room_id = request.args.get('room')
    matches = db.session.query(Matches).filter_by(id_sala = room_id).order_by(Matches.Ordem).all()
    if matches is None:
        return jsonify({'error': 'Partida não encontrada'}), 404
    return jsonify ([match.to_json() for match in matches]), 200
