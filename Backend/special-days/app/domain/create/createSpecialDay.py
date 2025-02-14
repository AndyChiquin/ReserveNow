from app.models.models import db, SpecialDay  # ✅ SRP: Handles only database interactions and model.
from flask import request, jsonify

def validate_special_day_data(data):
    """✅ SRP: Function responsible only for validating the request data."""
    if not data.get("date") or not data.get("event_name"):
        return "date and event_name are required"
    return None  # No validation errors

def create_special_day():
    """✅ SRP: Function responsible only for creating a special day entry."""
    try:
        data = request.json
        
        # ✅ SRP: Data validation is delegated to a separate function.
        validation_error = validate_special_day_data(data)
        if validation_error:
            return jsonify({"error": validation_error}), 400

        # ✅ SRP: Creating the new special day is handled separately.
        new_day = SpecialDay(
            date=data["date"],
            event_name=data["event_name"],
            description=data.get("description", "")
        )
        
        db.session.add(new_day)
        db.session.commit()

        return jsonify({"message": "Special day added!", "id": new_day.id}), 201

    except Exception as e:
        db.session.rollback()  # ✅ SRP: Error handling is focused on the transaction itself.
        return jsonify({"error": str(e)}), 500
