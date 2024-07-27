from flask import Blueprint, request, jsonify
from models.flight import insert_flight, get_flights

flight_status_bp = Blueprint('flight_status', __name__)

@flight_status_bp.route('/flights', methods=['GET'])
def get_all_flights():
    flights = get_flights()
    return jsonify(flights), 200

@flight_status_bp.route('/flights', methods=['POST'])
def add_flight():
    flight_data = request.json
    flight_id = insert_flight(flight_data)
    return jsonify({'id': str(flight_id)}), 201
