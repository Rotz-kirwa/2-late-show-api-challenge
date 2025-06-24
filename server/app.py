from flask import Flask, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from server.models import db
from server.controllers.auth_controller import auth_bp
from server.controllers.guest_controller import guest_bp
from server.controllers.episode_controller import episode_bp
from server.controllers.appearance_controller import appearance_bp

app = Flask(__name__)
app.config.from_pyfile("config.py")

CORS(app, supports_credentials=True)

migrate = Migrate()
jwt = JWTManager()

db.init_app(app)
migrate.init_app(app, db)
jwt.init_app(app)

app.register_blueprint(auth_bp)
app.register_blueprint(guest_bp)
app.register_blueprint(episode_bp)
app.register_blueprint(appearance_bp)

@app.route('/')
def index():
    return '''
    <html>
    <head>
        <title>Late Show API</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            .endpoint { margin-bottom: 15px; }
            button { margin-left: 10px; }
        </style>
        <script>
        function copyUrl(url) {
            navigator.clipboard.writeText(url);
            alert('Copied: ' + url);
        }
        </script>
    </head>
    <body>
        <h1>Late Show API Endpoints</h1>
        <div class="endpoint">
            <b>Index:</b> <code>GET /</code>
            <button onclick="copyUrl('http://localhost:5000/')">Copy URL</button>
        </div>
        <div class="endpoint">
            <b>Auth - Login:</b> <code>POST /auth/login</code>
            <button onclick="copyUrl('http://localhost:5000/auth/login')">Copy URL</button>
        </div>
        <div class="endpoint">
            <b>Auth - Logout:</b> <code>DELETE /auth/logout</code>
            <button onclick="copyUrl('http://localhost:5000/auth/logout')">Copy URL</button>
        </div>
        <div class="endpoint">
            <b>Auth - Check Session:</b> <code>GET /auth/check_session</code>
            <button onclick="copyUrl('http://localhost:5000/auth/check_session')">Copy URL</button>
        </div>
        <div class="endpoint">
            <b>Guests:</b> <code>GET /guests/</code>
            <button onclick="copyUrl('http://localhost:5000/guests/')">Copy URL</button>
        </div>
        <div class="endpoint">
            <b>Episodes:</b> <code>GET /episodes/</code>
            <button onclick="copyUrl('http://localhost:5000/episodes/')">Copy URL</button>
        </div>
        <div class="endpoint">
            <b>Appearances:</b> <code>GET /appearances/</code>
            <button onclick="copyUrl('http://localhost:5000/appearances/')">Copy URL</button>
        </div>
    </body>
    </html>
    '''
