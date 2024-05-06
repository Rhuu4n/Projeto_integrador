from flask import Flask, request, jsonify
from models.models_users import User
from app import db
from app import bcrypt
from datetime import date
from datetime import datetime
from datetime import timedelta
from models.models_users import Token

import time

def set_users():
    new_user = request.get_json()

    o_user = User.from_json(new_user)
    o_user.senha = bcrypt.generate_password_hash(new_user.get("senha"))
    db.session.add(o_user)
    db.session.commit()

    return jsonify(o_user.to_json())

def get_users():
    Users = User.query.all()
    return jsonify ([user.to_json() for user in Users])

def del_users(id):
    d_user = db.get_or_404(User, id)
    db.session.delete(d_user)
    db.session.commit()

    return jsonify(d_user.to_json())

def get_user(user_id):
    user = User.query.filter(User.id == user_id).first()
        
    return jsonify(user.to_json())

def put_user(id):
    newput_user = request.get_json()
    p_user = db.get_or_404(User, id)

    p_user.nome = newput_user.get('nome')
    p_user.senha = newput_user.get("senha")
    p_user.email = newput_user.get("email")
    p_user.nascimento = newput_user.get("nascimento")


    db.session.commit()

    return jsonify(p_user.to_json()), 201

def login_user():
    body = request.get_json()

    id = body.get("id")
    Login = body.get("nome")
    Senha = body.get("senha")

    ouser = User.query.filter_by(nome=Login).first_or_404(description="Usuario não encontrado")
    if (bcrypt.check_password_hash(ouser.senha, Senha)):
        ts = str(time.time())
        token_a = Senha + ts
        expiration = date.today() + timedelta(hours=3)
        token = bcrypt.generate_password_hash(token_a)
        o_token = Token.from_json({
            'id': id,
            'token':token,
            'expiration_at': expiration
        })

        db.session.add(o_token)
        db.session.commit()

        return jsonify("Logado com sucesso!")
    else:
        return jsonify("Usuario ou senha incorretos"),401