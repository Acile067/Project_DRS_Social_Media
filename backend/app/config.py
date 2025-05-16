
import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads', 'images')
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

    MAIL_SERVER = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.getenv('MAIL_PORT', 587))
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS', 'true').lower() == 'true'
    MAIL_USE_SSL = os.getenv('MAIL_USE_SSL', 'false').lower() == 'true'
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER')

    FLASK_ENV = os.getenv('FLASK_ENV', 'development')
    FLASK_APP = os.getenv('FLASK_APP', 'run.py')

    CORS_ORIGINS = os.getenv('CORS_ORIGINS', '*')  # Za produkciju stavi pravu vrednost
