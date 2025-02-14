from app.models.models import db, SpecialDay  # ✅ DRY: Importing database and model once.
from flask import request, jsonify

def serialize_special_day(day):
    """✅ DRY: Function to convert special day object to a dictionary."""
    return {
        "id": day.id,
        "date": str(day.date),  # ✅ DRY: Ensuring date is always formatted consistently.
        "event_name": day.event_name,
        "description": day.description
    }

def get_all_special_days():
    """Retorna todos los días especiales almacenados en la base de datos"""
    try:
        special_days = SpecialDay.query.all()  # ✅ DRY: Retrieving all special days.
        result = [serialize_special_day(day) for day in special_days]  # ✅ DRY: Using the serialization function.
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_special_day_by_id(special_day_id):
    """Retorna un día especial por su ID"""
    try:
        special_day = SpecialDay.query.get(special_day_id)
        if not special_day:
            return jsonify({"error": "Special day not found"}), 404

        result = serialize_special_day(special_day)  # ✅ DRY: Reusing serialization function.
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
