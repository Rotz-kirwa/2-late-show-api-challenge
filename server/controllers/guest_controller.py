from flask import Blueprint, jsonify
from server.models import Guest

guest_bp = Blueprint('guest_bp', __name__, url_prefix='/guests')

@guest_bp.route('', methods=['GET'])
@guest_bp.route('/', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return jsonify([
        {
            "id": guest.id,
            "name": guest.name,
            "occupation": guest.occupation,
            "email": guest.email
        } for guest in guests
    ])
