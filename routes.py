from flask import Blueprint, request, jsonify
from models import db, User
from werkzeug.security import generate_password_hash
from flask_jwt_extended import create_access_token

api = Blueprint("api", __name__)

@api.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    if not data.get("name") or not data.get("email") or len(data.get("password", "")) < 6:
        return jsonify({"msg": "Datos inválidos"}), 400
    
    if User.query.filter_by(email=data["email"]).first():
        return jsonify({"msg": "Correo ya registrado"}), 400

    hashed = generate_password_hash(data["password"])
    new_user = User(name=data["name"], email=data["email"], password=hashed)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"msg": "Usuario registrado con éxito"}), 201

@api.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([{"name": u.name, "email": u.email} for u in users])
