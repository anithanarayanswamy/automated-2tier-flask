from flask import Blueprint, jsonify

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET'])
def index():
    return jsonify({
        "message": "Welcome to the Two-Tier Customer Sales Application",
        "endpoints": {
            "health": "/health",
            "customers": "/customers?name=<customer_name>"
        },
        "description": "This is a production-style two-tier web application designed to allow a client to view customer sales and purchase details by customer name."
    }), 200