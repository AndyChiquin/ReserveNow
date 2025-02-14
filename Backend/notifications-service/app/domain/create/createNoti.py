from flask import Blueprint, request, jsonify
from app.models import Notification
from app.config.settings import db
from datetime import datetime

create_notification_bp = Blueprint('create_notification', __name__)

@create_notification_bp.route('/notification', methods=['POST'])
def create_notification_route():
    data = request.get_json()
    
    user_id = data.get('user_id')
    message = data.get('message')
    status = data.get('status')
    
    if not user_id or not message or not status:
        return jsonify({"error": "Missing required fields"}), 400

    new_notification = Notification(
        user_id=user_id,
        message=message,
        date=datetime.now(),
        status=status
    )

    db.session.add(new_notification)
    db.session.commit()

    return jsonify({"message": "Notification created successfully!"}), 201
