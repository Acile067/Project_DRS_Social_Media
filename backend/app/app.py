from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
#from flask_mail import Mail  # Import Flask-Mail

# Initialize the database and mail
db = SQLAlchemy()
#mail = Mail()

def create_app():
    app = Flask(__name__, template_folder='templates')

    # Configure SQLAlchemy (MySQL database)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:MySQLPassword1@127.0.0.1/appDB'


    # Flask-Mail configuration for email sending
    #app.config['MAIL_SERVER'] = 'smtp.hushmail.com'  # SMTP server
    #app.config['MAIL_PORT'] = 587
    #app.config['MAIL_USE_TLS'] = True
    #app.config['MAIL_USE_SSL'] = False
    #app.config['MAIL_USERNAME'] = 'hehido1992@lineacr.com'  # Your admin email address
    #app.config['MAIL_PASSWORD'] = ''  # Your email password or app password
    #app.config['MAIL_DEFAULT_SENDER'] = 'hehido1992@lineacr.com'

    # Initialize the extensions
    db.init_app(app)
    #mail.init_app(app)  # Initialize Flask-Mail

    # Enable Cross-Origin Resource Sharing (CORS)
    CORS(app)

    # Register blueprints
    from app.blueprints.users.routes import users_bp
    app.register_blueprint(users_bp, url_prefix='/user')

    from app.blueprints.posts.routes import posts_bp
    app.register_blueprint(posts_bp, url_prefix='/post')



    # Initialize Flask-Migrate for database migrations
    migrate = Migrate(app, db)

    return app
