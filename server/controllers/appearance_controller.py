from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from server.models import Appearance, db

appearance_bp = Blueprint('appearance_bp', __name__, url_prefix='/appearances')

@appearance_bp.route('', methods=['GET'])
@appearance_bp.route('/', methods=['GET'])
def get_appearances():
    appearances = Appearance.query.all()
    return jsonify([
        {
            "id": appearance.id,
            "rating": appearance.rating,
            "guest_id": appearance.guest_id,
            "episode_id": appearance.episode_id
        } for appearance in appearances
    ])

@appearance_bp.route('/', methods=['POST'])
@jwt_required()
def create_appearance():
    data = request.get_json()
    rating = data.get('rating')
    guest_id = data.get('guest_id')
    episode_id = data.get('episode_id')
    if not (1 <= rating <= 5):
        return jsonify({'error': 'Rating must be 1-5'}), 400
    appearance = Appearance(rating=rating, guest_id=guest_id, episode_id=episode_id)
    db.session.add(appearance)
    db.session.commit()
    return jsonify({'message': 'Appearance created', 'id': appearance.id}), 201
