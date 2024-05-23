from flask_http_middleware import MiddlewareManager, BaseHTTPMiddleware
from flask import Flask, request, jsonify
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
        if (request.path in self.secured_routers):
            now = datetime.now()
            token_ex = Token.query.filter(Token.expiration_at >= now).filter_by(token = request.headers.get("token")).first()

            if(token_ex == None):
               return jsonify({"error":"Usuario nao autenticado"})
            else:
                return call_next(request)
            


            #query token experation
            #if (request.headers.get('token') == 'Guilty123@@'):
            #    return call_next(request)
            #else:
           #     return jsonify({"error":"Usuario não autenticado"})
        else:
            return call_next(request)
    

        