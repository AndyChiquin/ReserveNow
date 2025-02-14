from flask import Blueprint, jsonify
from app.models import Notification
from app.config.settings import db

delete_notification_bp = Blueprint('delete_notification', __name__)

@delete_notification_bp.route('/notification/<int:notification_id>', methods=['DELETE'])
def delete_notification_route(notification_id):
    notification = Notification.query.get(notification_id)
    
    if not notification:
        return jsonify({"error": "Notification not found"}), 404
    
    db.session.delete(notification)
    db.session.commit()

    return jsonify({"message": "Notification deleted successfully!"}), 200
