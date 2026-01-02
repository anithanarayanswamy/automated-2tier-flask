import os
import time
from sqlalchemy import text
from app import create_app, db
from app.services.customer_service import initialize_sample_data

def create_app_with_data():
    app = create_app()

    # Wait for database to be ready
    max_retries = 30
    retry_count = 0
    db_ready = False

    while retry_count < max_retries and not db_ready:
        try:
            with app.app_context():
                # Test database connection
                db.session.execute(text('SELECT 1'))
                print("Database connection successful!")
                db.create_all()
                initialize_sample_data()
                db_ready = True
        except Exception as e:
            print(f"Database not ready, waiting... (attempt {retry_count + 1}/{max_retries}) Error: {e}")
            retry_count += 1
            time.sleep(2)  # Wait 2 seconds before retrying

    if not db_ready:
        print("Failed to connect to database after maximum retries")
        raise Exception("Database connection failed")

    return app

def main():
    app = create_app_with_data()

    # Run the application
    app.run(debug=os.environ.get('FLASK_DEBUG', 'False').lower() == 'true',
            host='0.0.0.0',
            port=int(os.environ.get('PORT', 5000)))

if __name__ == '__main__':
    main()