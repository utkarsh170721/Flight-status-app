# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Mock flight data
flights = [
    {'id': '6E 2341', 'status': 'On Time', 'gate': 'A12', 'departure_time': '2024-07-26T14:00:00Z'},
    # Add more flights here
]

@app.route('/flights', methods=['GET'])
def get_flights():
    return jsonify(flights)

@app.route('/flights/<string:flight_id>/status', methods=['GET'])
def get_flight_status(flight_id):
    flight = next((f for f in flights if f['id'] == flight_id), None)
    if flight:
        return jsonify(flight)
    return jsonify({'error': 'Flight not found'}), 404

@app.route('/flights/<string:flight_id>/update', methods=['POST'])
def update_flight_status(flight_id):
    flight = next((f for f in flights if f['id'] == flight_id), None)
    if flight:
        flight['status'] = request.json['status']
        flight['gate'] = request.json['gate']
        flight['departure_time'] = request.json['departure_time']
        return jsonify(flight)
    return jsonify({'error': 'Flight not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)