from flask import Blueprint, jsonify
from app.models.menu import db, Menu  # ✅ KISS: Importing only the necessary modules.

delete_menu_bp = Blueprint('delete_menu', __name__)

@delete_menu_bp.route('/menu/<int:menu_id>', methods=['DELETE'])
def delete_menu(menu_id):
    """✅ KISS: Simple and direct function to delete a menu item."""
    
    menu_item = Menu.query.get(menu_id)  # ✅ KISS: Direct database query to get the menu item.

    if not menu_item:
        return jsonify({"message": "Menu item not found"}), 404  # ✅ KISS: Simple and clear response.

    db.session.delete(menu_item)
    db.session.commit()  # ✅ KISS: Straightforward database transaction.

    return jsonify({"message": "Menu item deleted successfully"})  # ✅ KISS: Clear and concise success message.
