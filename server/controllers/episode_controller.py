from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from server.models import Episode, Appearance, db

episode_bp = Blueprint('episode_bp', __name__, url_prefix='/episodes')

@episode_bp.route('', methods=['GET'])
@episode_bp.route('/', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([
        {
            "id": episode.id,
            "date": episode.date.isoformat() if episode.date else None,
            "number": episode.number
        } for episode in episodes
    ])

@episode_bp.route('/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get_or_404(id)
    appearances = Appearance.query.filter_by(episode_id=episode.id).all()
    return jsonify({
        "id": episode.id,
        "date": episode.date.isoformat() if episode.date else None,
        "number": episode.number,
        "appearances": [
            {
                "id": a.id,
                "rating": a.rating,
                "guest_id": a.guest_id
            } for a in appearances
        ]
    })

@episode_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_episode(id):
    episode = Episode.query.get_or_404(id)
    # Cascade delete appearances
    Appearance.query.filter_by(episode_id=episode.id).delete()
    db.session.delete(episode)
    db.session.commit()
    return jsonify({'message': 'Episode and its appearances deleted'})
