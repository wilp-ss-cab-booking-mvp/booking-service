from flask import Flask
from flask_jwt_extended import JWTManager
from models import db
from routes import bp
from config import DB_URI, JWT_SECRET

app = Flask(__name__)

# App configuration
app.config["SQLALCHEMY_DATABASE_URI"] = DB_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = JWT_SECRET

# Initialize database
db.init_app(app)
with app.app_context():
    db.create_all()

# Register JWT and Blueprint (routes)
JWTManager(app)
app.register_blueprint(bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)