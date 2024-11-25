from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_mail import Mail
# Initialize the database
db = SQLAlchemy()
mail = Mail()

def create_app():
    app = Flask(__name__, template_folder='templates')

    # Configure SQLAlchemy (MySQL database)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:MySQLPassword1@127.0.0.1/appDB'
    UPLOAD_FOLDER = 'uploads/images'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

    # Mail configuration
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL '] = False
    app.config['MAIL_USERNAME'] = 'aleksandarsasastefanjovana@gmail.com'  # Postavite vaš email
    app.config['MAIL_PASSWORD'] = 'ilpl posz pbee odrr'  # Postavite vašu lozinku
    app.config['MAIL_DEFAULT_SENDER'] = 'aleksandarsasastefanjovana@gmail.com'

    db.init_app(app)
    mail.init_app(app)

    # Enable Cross-Origin Resource Sharing (CORS)
    CORS(app)

    # Register blueprints
    from app.blueprints.users.routes import users_bp
    app.register_blueprint(users_bp, url_prefix='/user')

    from app.blueprints.posts.routes import posts_bp
    app.register_blueprint(posts_bp, url_prefix='/post')

    from app.blueprints.relationships.routes import relationships_bp
    app.register_blueprint(relationships_bp, url_prefix='/relationships')

    migrate = Migrate(app, db)

    return app
