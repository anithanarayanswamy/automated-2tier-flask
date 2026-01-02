from app.models.customer import Customer, Purchase
from app import db
from datetime import datetime

def get_customer_purchases(customer_name):
    """
    Retrieve customer details along with their purchase history
    """
    customer = Customer.query.filter(Customer.name.ilike(f'%{customer_name}%')).first()
    
    if customer:
        purchases = Purchase.query.filter_by(customer_id=customer.id).all()
        return {
            "customer": customer.name,
            "purchases": [purchase.to_dict() for purchase in purchases]
        }
    return None

def initialize_sample_data():
    """
    Initialize the database with sample data
    """
    # Check if data already exists
    if Customer.query.first() is not None:
        print("Sample data already exists, skipping initialization.")
        return
    
    # Create sample customers
    customer1 = Customer(name="John Doe", email="john@example.com")
    customer2 = Customer(name="Jane Smith", email="jane@example.com")
    customer3 = Customer(name="Bob Johnson", email="bob@example.com")
    
    # Add customers to session
    db.session.add(customer1)
    db.session.add(customer2)
    db.session.add(customer3)
    
    # Commit to get IDs for foreign key relationships
    db.session.commit()
    
    # Create sample purchases
    purchase1 = Purchase(
        product="Laptop",
        amount=1200.00,
        date=datetime(2024, 1, 15).date(),
        customer_id=customer1.id
    )
    
    purchase2 = Purchase(
        product="Mouse",
        amount=25.99,
        date=datetime(2024, 1, 20).date(),
        customer_id=customer1.id
    )
    
    purchase3 = Purchase(
        product="Keyboard",
        amount=75.50,
        date=datetime(2024, 2, 10).date(),
        customer_id=customer1.id
    )
    
    purchase4 = Purchase(
        product="Monitor",
        amount=300.00,
        date=datetime(2024, 3, 5).date(),
        customer_id=customer2.id
    )
    
    purchase5 = Purchase(
        product="Webcam",
        amount=89.99,
        date=datetime(2024, 3, 12).date(),
        customer_id=customer2.id
    )
    
    purchase6 = Purchase(
        product="Desk Chair",
        amount=150.00,
        date=datetime(2024, 4, 1).date(),
        customer_id=customer3.id
    )
    
    # Add purchases to session
    db.session.add(purchase1)
    db.session.add(purchase2)
    db.session.add(purchase3)
    db.session.add(purchase4)
    db.session.add(purchase5)
    db.session.add(purchase6)
    
    # Commit all changes
    db.session.commit()
    
    print("Sample data initialized successfully!")