SQLALCHEMY_DATABASE_URI = "postgresql://postgres:empire@localhost:5432/late_show_db"
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Session config
SECRET_KEY = 'super-secret-key'  # Needed for session-based auth
SESSION_TYPE = 'filesystem'      # Stores sessions on the file system (you can keep this or remove if not using Flask-Session)

# JWT config (optional, but included for completeness)
JWT_SECRET_KEY = 'super-jwt-secret'  # If you plan to use JWT in future

# CORS (needed only if you’re making requests from a frontend on another domain)
CORS_SUPPORTS_CREDENTIALS = True
