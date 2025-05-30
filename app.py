from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from models import db
from config import Config
from routes import api


app = Flask(__name__)
CORS(app)
app.config.from_object(Config)


db.init_app(app)
app.register_blueprint(api, url_prefix="/api")
#app.register_blueprint(api)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
