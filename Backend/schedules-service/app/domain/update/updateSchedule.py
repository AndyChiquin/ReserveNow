from flask import request, jsonify
from app.config.settings import db
from app.models.models import Schedule
from datetime import datetime

# ✅ SRP: Function responsible only for validating the schedule data.
def validate_schedule_data(data):
    day_of_week = data.get('day_of_week')
    opening_time = datetime.strptime(data.get('opening_time'), "%H:%M").time()
    closing_time = datetime.strptime(data.get('closing_time'), "%H:%M").time()
    special_day_id = data.get('special_day_id', None)
    return day_of_week, opening_time, closing_time, special_day_id

# ✅ SRP: Function responsible only for updating the schedule fields in the database.
def update_schedule_in_db(schedule, day_of_week, opening_time, closing_time, special_day_id):
    schedule.day_of_week = day_of_week
    schedule.opening_time = opening_time
    schedule.closing_time = closing_time
    schedule.special_day_id = special_day_id
    db.session.commit()

# Update schedule
def update_schedule(schedule_id):
    try:
        # ✅ KISS: Get data from the request and validate it.
        data = request.get_json()

        # ✅ DRY: Validating data using a helper function.
        day_of_week, opening_time, closing_time, special_day_id = validate_schedule_data(data)

        # ✅ KISS: Searching for the schedule to update.
        schedule = db.session.query(Schedule).filter(Schedule.id == schedule_id).first()

        if not schedule:
            return jsonify({'message': 'Schedule not found.'}), 404

        # ✅ DRY: Updating schedule fields using a helper function.
        update_schedule_in_db(schedule, day_of_week, opening_time, closing_time, special_day_id)

        return jsonify({
            'message': 'Schedule updated successfully.',
            'data': {
                'id': schedule.id,
                'day_of_week': schedule.day_of_week,
                'opening_time': schedule.opening_time.strftime("%H:%M"),
                'closing_time': schedule.closing_time.strftime("%H:%M"),
                'special_day_id': schedule.special_day_id
            }
        }), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Error updating schedule', 'error': str(e)}), 500
