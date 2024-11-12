from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:MySQLPassword1@127.0.0.1/appDB'

    db.init_app(app)

    CORS(app)

    from app.blueprints.users.routes import users_bp

    app.register_blueprint(users_bp, url_prefix='/user')

    migrate = Migrate(app, db)

    return app
