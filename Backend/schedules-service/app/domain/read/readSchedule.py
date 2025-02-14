from flask import request, jsonify
from app.config.settings import db
from app.models.models import Schedule

# ✅ SRP: Function responsible only for fetching schedules by restaurant_id.
def get_schedules_by_restaurant_id(restaurant_id):
    """Get schedules for a specific restaurant."""
    return db.session.query(Schedule).filter(Schedule.restaurant_id == restaurant_id).all()

# ✅ SRP: Function responsible only for formatting schedules for the response.
def format_schedules_for_response(schedules):
    """Format schedules to a response-friendly structure."""
    return [
        {
            'id': schedule.id,
            'day_of_week': schedule.day_of_week,
            'opening_time': schedule.opening_time.strftime("%H:%M"),
            'closing_time': schedule.closing_time.strftime("%H:%M"),
            'special_day_id': schedule.special_day_id
        }
        for schedule in schedules
    ]

# Read schedules
def read_schedules():
    try:
        # ✅ KISS: Get restaurant_id from query parameters and validate.
        restaurant_id = request.args.get('restaurant_id', type=int)

        if not restaurant_id:
            return jsonify({'message': 'Restaurant ID is required.'}), 400

        # ✅ DRY: Fetch schedules using a helper function.
        schedules = get_schedules_by_restaurant_id(restaurant_id)

        if not schedules:
            return jsonify({'message': 'No schedules found for the restaurant.'}), 404

        # ✅ DRY: Format the schedules using a helper function.
        schedules_list = format_schedules_for_response(schedules)

        return jsonify({'schedules': schedules_list}), 200

    except Exception as e:
        return jsonify({'message': 'Error fetching schedules', 'error': str(e)}), 500
