from app.models.models import db, SpecialDay  # ✅ OCP: Database interaction is abstracted through the model.
from flask import request, jsonify

def update_special_day_data(special_day, data):
    """✅ OCP: Function responsible only for updating the special day fields."""
    if "date" in data:
        special_day.date = data["date"]
    if "event_name" in data:
        special_day.event_name = data["event_name"]
    if "description" in data:
        special_day.description = data.get("description", special_day.description)

def update_special_day(special_day_id):
    """Actualiza un día especial por su ID"""
    try:
        data = request.json
        special_day = SpecialDay.query.get(special_day_id)

        if not special_day:
            return jsonify({"error": "Special day not found"}), 404

        # ✅ OCP: Delegating the update logic to a separate function.
        update_special_day_data(special_day, data)
        
        db.session.commit()

        return jsonify({"message": "Special day updated!", "id": special_day.id}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
