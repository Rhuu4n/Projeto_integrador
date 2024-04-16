from flask_http_middleware import MiddlewareManager, BaseHTTPMiddleware
from flask import Flask, request, jsonify


class MetricsMinddleware(BaseHTTPMiddleware):
    def __init__(self, secured_routers = []):
        super().__init__()
        self.secured_routers = secured_routers

    def dispatch(self, request, call_next):
        if not (request.path in self.secured_routers):
            if (request.headers.get('token') == 'Guilty123@@'):
                return call_next(request)
            else:
                return jsonify({"error":"Usuario não autenticado"})
        else:
            return call_next(request)
    

        