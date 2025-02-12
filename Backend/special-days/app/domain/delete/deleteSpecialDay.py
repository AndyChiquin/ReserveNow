from app.models.models import db, SpecialDay
from flask import request, jsonify

def delete_special_day(special_day_id):
    """Elimina un día especial por su ID"""
    try:
        special_day = SpecialDay.query.get(special_day_id)

        if not special_day:
            return jsonify({"error": "Special day not found"}), 404

        db.session.delete(special_day)
        db.session.commit()

        return jsonify({"message": "Special day deleted!", "id": special_day_id}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
