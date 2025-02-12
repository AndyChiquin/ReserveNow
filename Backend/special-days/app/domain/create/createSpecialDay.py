from app.models.models import db, SpecialDay
from flask import request, jsonify

def create_special_day():
    try:
        data = request.json
        if not data.get("date") or not data.get("event_name"):
            return jsonify({"error": "date and event_name are required"}), 400

        new_day = SpecialDay(
            date=data["date"],
            event_name=data["event_name"],
            description=data.get("description", "")
        )
        
        db.session.add(new_day)
        db.session.commit()
        
        return jsonify({"message": "Special day added!", "id": new_day.id}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
