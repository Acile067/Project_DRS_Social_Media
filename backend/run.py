from app.app import create_app, socketio
from dotenv import load_dotenv

load_dotenv()

flask_app = create_app()

if __name__ == "__main__":
    socketio.run(flask_app, host='0.0.0.0', debug=True, allow_unsafe_werkzeug=True)
