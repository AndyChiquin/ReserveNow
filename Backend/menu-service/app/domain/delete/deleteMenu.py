from flask import Blueprint, jsonify
from app.models.menu import db, Menu

delete_menu_bp = Blueprint('delete_menu', __name__)

@delete_menu_bp.route('/menu/<int:menu_id>', methods=['DELETE'])
def delete_menu(menu_id):
    menu_item = Menu.query.get(menu_id)

    if not menu_item:
        return jsonify({"message": "Menu item not found"}), 404

    db.session.delete(menu_item)
    db.session.commit()

    return jsonify({"message": "Menu item deleted successfully"})
