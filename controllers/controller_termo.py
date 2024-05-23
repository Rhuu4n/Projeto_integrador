from flask import Flask, request, jsonify
from models.models_termo import Palavra
from app import db
from app import bcrypt
from datetime import date
from datetime import datetime
from datetime import timedelta

import time

def set_termo():
    new_palavra = request.get_json()

    palavra = Palavra.from_json(new_palavra)
    db.session.add(palavra)
    db.session.commit()

    return jsonify(palavra.to_json()), 201 

def get_palavras():
    Termo = Palavra.query.all()
    return jsonify ([palavra.to_json() for palavra in Termo])

def del_termo(id):
    d_palavra = db.get_or_404(Palavra, id)
    db.session.delete(d_palavra)
    db.session.commit()

    return jsonify(d_palavra.to_json())

def get_termo(termo_id):
    palavra = Palavra.query.filter(Palavra.id == termo_id).first()
        
    return jsonify(palavra.to_json())

def put_termo(id):
    newput_palavra = request.get_json()
    p_palavra = db.get_or_404(Palavra, id)

    p_palavra.palavra = newput_palavra.get('palavra')

    db.session.commit()

    return jsonify(p_palavra.to_json()), 201