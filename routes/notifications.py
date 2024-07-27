from flask import Blueprint, request, jsonify
from models.notification import insert_flight, get_flights

notifications_bp = Blueprint('notifications', __name__)

@notifications_bp.route('/notifications', methods=['GET'])
def get_all_notifications():
    notifications = get_notifications()
    return jsonify(notifications), 200

@notifications_bp.route('/notifications', methods=['POST'])
def add_notification():
    notification_data = request.json
    notification_id = insert_notification(notification_data)
    return jsonify({'id': str(notification_id)}), 201
