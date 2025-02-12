from app.models.models import db, SpecialDay
from flask import request, jsonify

def get_all_special_days():
    """Retorna todos los días especiales almacenados en la base de datos"""
    try:
        special_days = SpecialDay.query.all()
        result = [
            {"id": day.id, "date": str(day.date), "event_name": day.event_name, "description": day.description}
            for day in special_days
        ]
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_special_day_by_id(special_day_id):
    """Retorna un día especial por su ID"""
    try:
        special_day = SpecialDay.query.get(special_day_id)
        if not special_day:
            return jsonify({"error": "Special day not found"}), 404

        result = {
            "id": special_day.id,
            "date": str(special_day.date),
            "event_name": special_day.event_name,
            "description": special_day.description
        }
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
