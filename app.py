from flask import Flask, request, jsonify

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()

def create_app():
    from routes.routes_users import bp_users
    from routes.routes_matches import bp_matches
    from routes.routes_rooms import bp_rooms
    from routes.routes_termo import bp_termo
    from flask_http_middleware import MiddlewareManager
    from middleware.middleware import MetricsMinddleware
    from flask_cors import CORS

    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*", "allow_headers": ["Content-Type", "Token"]}})
    
    app.register_blueprint(bp_users)
    app.register_blueprint(bp_matches)
    app.register_blueprint(bp_rooms) 
    app.register_blueprint(bp_termo)


    app.wsgi_app = MiddlewareManager(app)
    

    secured_routers = ["/login"]
    
    app.wsgi_app.add_middleware(MetricsMinddleware, secured_routers=secured_routers)


    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://projeto:Ubuntu12!@localhost/Projeto'

    db.init_app(app)
    migrate.init_app(app, db)
    global bcrypt
    bcrypt.init_app(app)
    
    return app
    # -h ip  -u -p 
