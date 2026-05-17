from flask import Flask, jsonify
from flask_cors import CORS
from routes.auth_routes import auth_bp
from routes.user_routes import user_routes
from routes.upload_routes import upload_routes
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "change-this-in-production")

allowed_origins = os.environ.get("ALLOWED_ORIGINS", "http://localhost:3000").split(",")
CORS(app, resources={r"/api/*": {"origins": allowed_origins}}, supports_credentials=True)

app.register_blueprint(auth_bp, url_prefix="/api/auth")
app.register_blueprint(user_routes, url_prefix="/api/user")
app.register_blueprint(upload_routes, url_prefix="/api")

@app.route("/", methods=["GET"])
def health_check():
    return jsonify({"message": "API is working!"}), 200

if __name__ == "__main__":
    os.makedirs("uploads", exist_ok=True)
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("FLASK_DEBUG", "true").lower() == "true"
    app.run(host="0.0.0.0", debug=debug, port=port)