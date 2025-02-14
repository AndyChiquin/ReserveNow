from flask import request, jsonify
from app.config.settings import db
from app.models.models import Schedule

# ✅ SRP: Function responsible only for fetching the schedule to delete.
def get_schedule_by_id(schedule_id):
    """Get a schedule by its ID."""
    return db.session.query(Schedule).filter(Schedule.id == schedule_id).first()

# ✅ SRP: Function responsible only for deleting the schedule from the database.
def delete_schedule_from_db(schedule):
    """Delete the schedule from the database."""
    db.session.delete(schedule)
    db.session.commit()

# Delete schedule
def delete_schedule(schedule_id):
    try:
        # ✅ KISS: Get the schedule to delete using a helper function.
        schedule = get_schedule_by_id(schedule_id)

        if not schedule:
            return jsonify({'message': 'Schedule not found.'}), 404

        # ✅ DRY: Deleting the schedule using a helper function.
        delete_schedule_from_db(schedule)

        return jsonify({'message': 'Schedule deleted successfully.'}), 200

    except Exception as e:
        db.session.rollback()  # ✅ KISS: Rollback transaction in case of an error.
        return jsonify({'message': 'Error deleting schedule', 'error': str(e)}), 500
