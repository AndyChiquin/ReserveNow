from flask import request, jsonify
from app.config.settings import db
from app.models.models import Schedule
from datetime import datetime

# ✅ SRP: Function responsible only for validating schedule data.
def validate_schedule_data(data):
    day_of_week = data.get('day_of_week')
    opening_time = datetime.strptime(data.get('opening_time'), "%H:%M").time()
    closing_time = datetime.strptime(data.get('closing_time'), "%H:%M").time()
    special_day_id = data.get('special_day_id', None)
    return day_of_week, opening_time, closing_time, special_day_id

# ✅ SRP: Function responsible for creating a new schedule.
def create_new_schedule(day_of_week, opening_time, closing_time, special_day_id):
    new_schedule = Schedule(
        day_of_week=day_of_week,
        opening_time=opening_time,
        closing_time=closing_time,
        special_day_id=special_day_id
    )
    db.session.add(new_schedule)
    db.session.commit()
    return new_schedule

# Create schedule
def create_schedule():
    try:
        # ✅ KISS: Getting data from request and validating it.
        data = request.get_json()

        day_of_week, opening_time, closing_time, special_day_id = validate_schedule_data(data)

        # ✅ DRY: Calling the function to create the new schedule.
        new_schedule = create_new_schedule(day_of_week, opening_time, closing_time, special_day_id)

        return jsonify({
            'message': 'Schedule created successfully.',
            'data': {
                'id': new_schedule.id,
                'day_of_week': new_schedule.day_of_week,
                'opening_time': new_schedule.opening_time,
                'closing_time': new_schedule.closing_time,
                'special_day_id': new_schedule.special_day_id
            }
        }), 201

    except Exception as e:
        db.session.rollback()  # ✅ KISS: Rolling back transaction if error occurs.
        return jsonify({'message': 'Error creating schedule', 'error': str(e)}), 500
