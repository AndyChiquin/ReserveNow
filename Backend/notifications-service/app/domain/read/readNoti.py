from flask import Blueprint, request, jsonify
from app.models import Notification
from app.config.settings import db

read_notification_bp = Blueprint('read_notification', __name__)

@read_notification_bp.route('/notification/<int:user_id>', methods=['GET'])
def get_notifications_route(user_id):
    notifications = Notification.query.filter_by(user_id=user_id).all()
    
    if not notifications:
        return jsonify({"error": "No notifications found"}), 404
    
    notifications_list = [{"id": notif.id, "message": notif.message, "date": notif.date, "status": notif.status} for notif in notifications]
    return jsonify(notifications_list), 200
