from app.models.models import db, SpecialDay  # ✅ KISS: Simple import for model and database.

from flask import request, jsonify

def delete_special_day(special_day_id):
    """✅ KISS: Simple function to delete a special day by its ID."""
    try:
        special_day = SpecialDay.query.get(special_day_id)  # ✅ KISS: Direct query to fetch the special day by ID.

        if not special_day:
            return jsonify({"error": "Special day not found"}), 404  # ✅ KISS: Clear and simple error handling.

        db.session.delete(special_day)  # ✅ KISS: Direct deletion without unnecessary steps.
        db.session.commit()  # ✅ KISS: Simple commit to finalize the deletion.

        return jsonify({"message": "Special day deleted!", "id": special_day_id}), 200  # ✅ KISS: Simple success message.

    except Exception as e:
        db.session.rollback()  # ✅ KISS: Rollback in case of any error.
        return jsonify({"error": str(e)}), 500  # ✅ KISS: Clear error response.
