#!/usr/bin/env python
"""
Script to initialize the database with sample data
"""
import sys
import os
from app import create_app, db
from app.services.customer_service import initialize_sample_data

# Load environment variables from .env file
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    print("python-dotenv not installed, skipping .env file loading")

def init_db():
    # Use database URL from environment variables
    database_url = os.environ.get('DATABASE_URL')

    # Create app with the database URL
    app = create_app()

    try:
        with app.app_context():
            # Test database connection
            db.engine.connect()
            print("Database connection successful!")

            db.create_all()
            initialize_sample_data()
            print("Database initialized with sample data!")

    except Exception as e:
        print(f"Database connection failed: {e}")
        print("\nMake sure your database is running. You can:")
        print("1. For MySQL: Start MySQL service: sudo systemctl start mysql")
        print("2. For SQLite: Make sure the path is correct in your DATABASE_URL")
        print("3. Or run with Docker: docker-compose up --build")
        print("4. Or update your DATABASE_URL in .env file")
        sys.exit(1)

if __name__ == '__main__':
    init_db()