from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# Initialize extensions
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configuration
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')

    # Use SQLite for development, MySQL for production
    database_url = os.environ.get('DATABASE_URL')
    if not database_url:
        # Check if we're in a production environment
        if os.environ.get('FLASK_ENV') == 'production':
            database_url = 'mysql+pymysql://root:password@localhost:3306/customerdb'
        else:
            # Use SQLite for local development
            database_url = 'sqlite:///customer_sales.db'

    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions with app
    db.init_app(app)

    # Register blueprints
    from app.routes.main import main_bp
    from app.routes.health import health_bp
    from app.routes.customers import customers_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(health_bp)
    app.register_blueprint(customers_bp)

    return app