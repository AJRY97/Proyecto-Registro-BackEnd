from flask import Blueprint, request, jsonify
from models import db, User
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash


api = Blueprint("api", __name__)

"""Registrar usuario"""
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

"""Obtener usuarios"""
@api.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([u.serialize() for u in users]), 200


"""Actualizar usuario"""
@api.route("/users/<int:id>", methods=["PUT"])
def update_user(id):
    data = request.get_json()
    user = User.query.get(id)

    if not user:
        return jsonify({"error": "Usuario no encontrado"}), 404

    if not data.get("password"):
        return jsonify({"error": "La contraseña es requerida"}), 400
    data = request.get_json()
    print("Contraseña recibida:", data.get("password"))
    print("Contraseña guardada:", user.password)

    if not check_password_hash(user.password, data["password"]):
        return jsonify({"error": "Contraseña incorrecta"}), 401


    user.name = data.get("name", user.name)
    user.email = data.get("email", user.email)

    db.session.commit()
    return jsonify(user.serialize()), 200


"""Eliminar usuario"""
@api.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({"msg": "Usuario no encontrado"}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({"msg": "Usuario eliminado correctamente"}), 200