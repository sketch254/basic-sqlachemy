from flask import Blueprint, jsonify, request

from models.profile import Profile
from models.user import User

from services.service import save, fetch # routes never import db

bp = Blueprint("user_profile", __name__)

@bp.route("/user", methods=["POST"])
def create_user_handler():
    body = request.get_json()
    obj = User(**body)
    save(obj)
    return jsonify(obj.to_dict()), 201

@bp.route("/user/<int:pk>", methods=["GET"])
def read_user_handler(pk):
    result = fetch(User, pk)
    if result is None:
        return jsonify({"error": "Not found"}), 404
    return jsonify(result.to_dict())

@bp.route("/profile", methods=["POST"])
def create_handler():
    body = request.get_json()
    obj = Profile(**body)
    save(obj)
    return jsonify(obj.to_dict()), 201

@bp.route("/profile/<int:pk>", methods=["GET"])
def read_handler(pk):
    result = fetch(User, pk)
    if result is None:
        return jsonify({"error": "Not found"}), 404
    return jsonify(result.to_dict())