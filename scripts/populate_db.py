#!/usr/bin/env python3
"""
Script to populate the database with sample data.
Creates 10 customers and 25 purchases as specified in the README.
"""

import os
import sys
import random
from datetime import datetime, timedelta
from decimal import Decimal

# Add the project root to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app, db
from app.models.customer import Customer, Purchase


def populate_database():
    """Populate the database with sample customers and purchases."""

    # Create Flask app instance with proper configuration
    app = create_app()

    with app.app_context():
        # Create all tables (if they don't exist)
        db.create_all()

        # Clear existing data to ensure we start fresh
        Purchase.query.delete()
        Customer.query.delete()
        db.session.commit()

        print("Cleared existing data. Populating with new sample data...")

        # Sample customer names and emails
        customer_data = [
            ("John Smith", "john.smith@example.com"),
            ("Emma Johnson", "emma.johnson@example.com"),
            ("Michael Williams", "michael.williams@example.com"),
            ("Sarah Brown", "sarah.brown@example.com"),
            ("David Jones", "david.jones@example.com"),
            ("Lisa Davis", "lisa.davis@example.com"),
            ("James Miller", "james.miller@example.com"),
            ("Jennifer Wilson", "jennifer.wilson@example.com"),
            ("Robert Taylor", "robert.taylor@example.com"),
            ("Patricia Anderson", "patricia.anderson@example.com")
        ]

        # Sample products
        products = [
            "Laptop", "Wireless Mouse", "Mechanical Keyboard", "Monitor",
            "Webcam", "Headphones", "USB-C Hub", "External Hard Drive",
            "Tablet", "Smartphone", "Bluetooth Speaker", "Smart Watch",
            "Gaming Controller", "Printer", "Scanner", "Router",
            "Smart TV", "Coffee Maker", "Blender", "Microwave",
            "Refrigerator", "Washing Machine", "Vacuum Cleaner", "Toaster",
            "Electric Kettle", "Air Fryer", "Pressure Cooker", "Dishwasher"
        ]

        # Create customers
        customers = []
        for name, email in customer_data:
            customer = Customer(name=name, email=email)
            db.session.add(customer)
            customers.append(customer)

        # Commit customers to get IDs for foreign key relationships
        db.session.commit()

        # Create 25 purchases distributed among the customers
        purchases = []
        for i in range(25):
            # Randomly select a customer
            customer = random.choice(customers)

            # Randomly select a product
            product = random.choice(products)

            # Generate a random amount between $10.00 and $1500.00
            amount = round(Decimal(random.uniform(10.00, 1500.00)), 2)

            # Generate a random date within the last year
            days_ago = random.randint(1, 365)
            date = (datetime.now() - timedelta(days=days_ago)).date()

            purchase = Purchase(
                product=product,
                amount=amount,
                date=date,
                customer_id=customer.id
            )

            db.session.add(purchase)
            purchases.append(purchase)

        # Commit all purchases
        db.session.commit()

        print(f"Successfully populated database with {len(customers)} customers and {len(purchases)} purchases.")

        # Print summary
        print("\nCustomer Summary:")
        for customer in customers:
            purchase_count = len(customer.purchases)
            print(f"- {customer.name}: {purchase_count} purchase(s)")

        print(f"\nTotal purchases: {len(purchases)}")


if __name__ == "__main__":
    populate_database()