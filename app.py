from flask import Flask, request, jsonify

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

# erick r
# k

def create_app():
    from routes.routes_users import bp_users
    from routes.routes_matches import bp_matches
    from routes.routes_rooms import bp_rooms

    app = Flask(__name__)

    app.register_blueprint(bp_users)
    app.register_blueprint(bp_matches)
    app.register_blueprint(bp_rooms) 

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://projeto:Ubuntu12!@10.60.46.21/Projeto'

    db.init_app(app)
    migrate.init_app(app, db)
    
    return app
    # -h ip  -u -p 
