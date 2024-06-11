from flask_http_middleware import MiddlewareManager, BaseHTTPMiddleware
from flask import Flask, request, jsonify, make_response
from datetime import date
from datetime import datetime
from datetime import timedelta
from models.models_users import Token
from app import db


class MetricsMinddleware(BaseHTTPMiddleware):
    def __init__(self, secured_routers = []):
        super().__init__()
        self.secured_routers = secured_routers

    def dispatch(self, request, call_next):
        if not (request.path in self.secured_routers):
            now = datetime.now()
            token_ex = Token.query.filter(Token.expiration_at >= now).filter_by(token = request.headers.get("token")).first()

            if(token_ex == None):
                response = make_response(jsonify({"error": "Usuario nao autenticado"}), 401)
                return response
        else:
            return call_next(request)
    

        