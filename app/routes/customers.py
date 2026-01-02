from flask import Blueprint, request, jsonify
from app.models.customer import Customer, Purchase
from app.services.customer_service import get_customer_purchases

customers_bp = Blueprint('customers', __name__)

@customers_bp.route('/customers', methods=['GET'])
def get_customers():
    customer_name = request.args.get('name')
    
    if not customer_name:
        return jsonify({"error": "Customer name is required"}), 400
    
    try:
        customer_data = get_customer_purchases(customer_name)
        if customer_data:
            return jsonify(customer_data), 200
        else:
            return jsonify({"error": "Customer not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500