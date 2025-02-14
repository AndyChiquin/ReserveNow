from flask import Blueprint, request, jsonify
from app.models import Notification
from app.config.settings import db

update_notification_bp = Blueprint('update_notification', __name__)

@update_notification_bp.route('/notification/<int:notification_id>', methods=['PUT'])
def update_notification_route(notification_id):
    data = request.get_json()

    # Buscar la notificación por ID
    notification = Notification.query.get(notification_id)
    
    if not notification:
        return jsonify({"error": "Notification not found"}), 404
    
    # Actualizar la notificación
    message = data.get('message', notification.message)
    status = data.get('status', notification.status)

    notification.message = message
    notification.status = status

    db.session.commit()

    return jsonify({"message": "Notification updated successfully!"}), 200
