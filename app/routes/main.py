from flask import Blueprint, jsonify, render_template, request
from app.services.customer_service import get_customer_purchases

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET'])
def index():
    return jsonify({
        "message": "Welcome to the Two-Tier Customer Sales Application",
        "endpoints": {
            "health": "/health",
            "customers": "/customers?name=<customer_name>",
            "customer_sales_lookup": "/customer-sales-lookup"
        },
        "description": "This is a production-style two-tier web application designed to allow a client to view customer sales and purchase details by customer name."
    }), 200

@main_bp.route('/customer-sales-lookup', methods=['GET', 'POST'])
def customer_sales_lookup():
    customer_name = request.args.get('name') if request.method == 'GET' else None
    customer_data = None

    if customer_name:
        try:
            customer_data = get_customer_purchases(customer_name)
        except Exception:
            # If customer not found, we'll just pass None to the template
            pass

    return render_template('customer_sales_lookup.html', customer_data=customer_data, customer_name=customer_name)