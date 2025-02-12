from app.models.models import db, SpecialDay
from flask import request, jsonify

def update_special_day(special_day_id):
    """Actualiza un día especial por su ID"""
    try:
        data = request.json
        special_day = SpecialDay.query.get(special_day_id)

        if not special_day:
            return jsonify({"error": "Special day not found"}), 404

        if "date" in data:
            special_day.date = data["date"]
        if "event_name" in data:
            special_day.event_name = data["event_name"]
        if "description" in data:
            special_day.description = data.get("description", special_day.description)

        db.session.commit()

        return jsonify({"message": "Special day updated!", "id": special_day.id}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
