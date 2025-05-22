
import os
import urllib

class Config:

    FLASK_ENV = os.getenv('FLASK_ENV', 'development')

    if (FLASK_ENV != 'development'):
        DB_PASSWORD = os.getenv('DB_PASSWORD')

        params = urllib.parse.quote_plus(
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER=tcp:sql-socialmediadrs-dev-eun-001.database.windows.net,1433;"
        f"DATABASE=sqldb-socialmediadrs-dev-eun-001;"
        f"UID=adminuser;"
        f"PWD={DB_PASSWORD};"
        f"Encrypt=yes;"
        f"TrustServerCertificate=no;"
        f"Connection Timeout=30;"
        )

        SQL_STRING = f"mssql+pyodbc:///?odbc_connect={params}"

        AZURE_STORAGE_ACCOUNT_NAME = os.getenv('AZURE_STORAGE_ACCOUNT_NAME')
        AZURE_STORAGE_CONTAINER = os.getenv('AZURE_STORAGE_CONTAINER')
        
    else:
        SQL_STRING = "mysql+mysqlconnector://root:MySQLPassword1@127.0.0.1/appDB"
    
    SQLALCHEMY_DATABASE_URI = SQL_STRING
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

    FLASK_APP = os.getenv('FLASK_APP', 'run.py')

    CORS_ORIGINS = os.getenv('CORS_ORIGINS', '*')  # Za produkciju stavi pravu vrednost
