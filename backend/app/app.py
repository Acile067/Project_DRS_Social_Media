from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_mail import Mail
from flask_socketio import SocketIO
from app.config import Config
from flask_migrate import upgrade

# Initialize the database
db = SQLAlchemy()
mail = Mail()
socketio = SocketIO(cors_allowed_origins=Config.CORS_ORIGINS)

def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config.from_object(Config)

    db.init_app(app)
    mail.init_app(app)

    # Initialize Socket.IO with CORS support
    socketio.init_app(app, cors_allowed_origins=Config.CORS_ORIGINS)
    CORS(app, resources={r"/*": {"origins": Config.CORS_ORIGINS}})

    # Register blueprints
    from app.blueprints.users.routes import users_bp
    app.register_blueprint(users_bp, url_prefix='/user')

    from app.blueprints.posts.routes import posts_bp
    app.register_blueprint(posts_bp, url_prefix='/post')

    from app.blueprints.relationships.routes import relationships_bp
    app.register_blueprint(relationships_bp, url_prefix='/relationships')

    migrate = Migrate(app, db)

    with app.app_context():
        upgrade()

    return app
