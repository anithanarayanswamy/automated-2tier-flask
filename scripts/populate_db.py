#!/usr/bin/env python
"""
Script to populate MySQL database with 10 sample data entries
"""
import os
import sys
from datetime import datetime, date
from app import create_app, db
from app.models.customer import Customer, Purchase

# Load environment variables from .env file
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    print("python-dotenv not installed, skipping .env file loading")

def populate_sample_data():
    # Use the database URL from environment variables
    database_url = os.environ.get('DATABASE_URL', 'sqlite:///customer_sales.db')
    
    # Create app with the database URL
    os.environ['DATABASE_URL'] = database_url
    app = create_app()
    
    with app.app_context():
        try:
            # Test database connection
            db.engine.connect()
            print("Database connection successful!")
        except Exception as e:
            print(f"Database connection failed: {e}")
            print("\nMake sure your database is running.")
            sys.exit(1)
        
        # Drop and recreate tables
        db.drop_all()
        db.create_all()
        
        # Create 10 sample customers with purchases
        sample_customers = [
            {
                "name": "John Doe",
                "email": "john.doe@example.com",
                "purchases": [
                    {"product": "Laptop", "amount": 1200.00, "date": date(2024, 1, 15)},
                    {"product": "Mouse", "amount": 25.99, "date": date(2024, 1, 20)},
                    {"product": "Keyboard", "amount": 75.50, "date": date(2024, 2, 10)}
                ]
            },
            {
                "name": "Jane Smith",
                "email": "jane.smith@example.com",
                "purchases": [
                    {"product": "Monitor", "amount": 300.00, "date": date(2024, 3, 5)},
                    {"product": "Webcam", "amount": 89.99, "date": date(2024, 3, 12)}
                ]
            },
            {
                "name": "Bob Johnson",
                "email": "bob.johnson@example.com",
                "purchases": [
                    {"product": "Desk Chair", "amount": 150.00, "date": date(2024, 4, 1)}
                ]
            },
            {
                "name": "Alice Williams",
                "email": "alice.williams@example.com",
                "purchases": [
                    {"product": "Smartphone", "amount": 899.99, "date": date(2024, 2, 28)},
                    {"product": "Phone Case", "amount": 29.99, "date": date(2024, 3, 1)}
                ]
            },
            {
                "name": "Charlie Brown",
                "email": "charlie.brown@example.com",
                "purchases": [
                    {"product": "Headphones", "amount": 199.99, "date": date(2024, 1, 10)},
                    {"product": "Charging Cable", "amount": 19.99, "date": date(2024, 1, 12)},
                    {"product": "Power Bank", "amount": 59.99, "date": date(2024, 2, 5)}
                ]
            },
            {
                "name": "Diana Miller",
                "email": "diana.miller@example.com",
                "purchases": [
                    {"product": "Tablet", "amount": 450.00, "date": date(2024, 4, 15)},
                    {"product": "Tablet Stand", "amount": 35.00, "date": date(2024, 4, 16)},
                    {"product": "Screen Protector", "amount": 15.99, "date": date(2024, 4, 17)}
                ]
            },
            {
                "name": "Ethan Davis",
                "email": "ethan.davis@example.com",
                "purchases": [
                    {"product": "Gaming Console", "amount": 499.99, "date": date(2024, 5, 10)},
                    {"product": "Gaming Controller", "amount": 69.99, "date": date(2024, 5, 12)}
                ]
            },
            {
                "name": "Fiona Garcia",
                "email": "fiona.garcia@example.com",
                "purchases": [
                    {"product": "Smart Watch", "amount": 299.99, "date": date(2024, 6, 5)},
                    {"product": "Watch Band", "amount": 25.00, "date": date(2024, 6, 6)},
                    {"product": "Wireless Charger", "amount": 39.99, "date": date(2024, 6, 8)}
                ]
            },
            {
                "name": "George Rodriguez",
                "email": "george.rodriguez@example.com",
                "purchases": [
                    {"product": "Bluetooth Speaker", "amount": 129.99, "date": date(2024, 7, 1)},
                    {"product": "Audio Cable", "amount": 19.99, "date": date(2024, 7, 3)}
                ]
            },
            {
                "name": "Helen Martinez",
                "email": "helen.martinez@example.com",
                "purchases": [
                    {"product": "Camera", "amount": 799.99, "date": date(2024, 8, 15)},
                    {"product": "Memory Card", "amount": 49.99, "date": date(2024, 8, 16)},
                    {"product": "Tripod", "amount": 89.99, "date": date(2024, 8, 18)},
                    {"product": "Camera Bag", "amount": 69.99, "date": date(2024, 8, 20)}
                ]
            }
        ]
        
        # Add customers and their purchases to the database
        for customer_data in sample_customers:
            customer = Customer(
                name=customer_data["name"],
                email=customer_data["email"]
            )
            db.session.add(customer)
            db.session.flush()  # Get the ID for the customer
            
            for purchase_data in customer_data["purchases"]:
                purchase = Purchase(
                    product=purchase_data["product"],
                    amount=purchase_data["amount"],
                    date=purchase_data["date"],
                    customer_id=customer.id
                )
                db.session.add(purchase)
        
        # Commit all changes
        db.session.commit()
        
        print("Database populated with 10 sample customers and their purchases!")
        print(f"Total customers: {len(sample_customers)}")
        total_purchases = sum(len(c["purchases"]) for c in sample_customers)
        print(f"Total purchases: {total_purchases}")

if __name__ == '__main__':
    populate_sample_data()