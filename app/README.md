# Two-Tier Customer Sales Application

This is a production-style two-tier web application built with Flask and MySQL that allows users to view customer sales and purchase details by customer name.

## Tech Stack

- Python 3
- Flask – REST API framework
- SQLAlchemy – ORM for database access
- MySQL 8 – Relational database
- Docker – Containerization
- Docker Compose – Local multi-service orchestration

## Project Structure

```
.
├── app/
│   ├── __init__.py          # Flask app factory
│   ├── routes/              # API routes (controllers)
│   │   ├── health.py
│   │   └── customers.py
│   ├── services/            # Business logic layer
│   │   └── customer_service.py
│   ├── models/              # Database models
│   │   └── customer.py
│   └── config/              # Environment-based configuration
│       └── settings.py
├── scripts/                 # Initialization scripts
│   └── init_db.py
├── run.py                   # Application entry point
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables
├── Dockerfile               # Docker configuration
└── docker-compose.yml       # Multi-container orchestration
```

## API Endpoints

### Health Check
```
GET /health
```

### Get Customer Purchase Details
```
GET /customers?name=<customer_name>
```

Example:
```
GET /customers?name=John
```

Response:
```json
{
  "customer": "John Doe",
  "purchases": [
    {
      "product": "Laptop",
      "amount": 1200.0,
      "date": "2024-01-15"
    }
  ]
}
```

## Setup and Running

### Local Development
1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set up environment variables (copy .env.example if needed):
   ```bash
   cp .env .env
   ```

3. Initialize the database:
   ```bash
   python scripts/init_db.py
   ```

4. Run the application:
   ```bash
   python run.py
   ```

The application will be available at `http://localhost:5000`

### Using Docker
1. Build and run with Docker Compose:
   ```bash
   docker-compose up --build
   ```

The application will be available at `http://localhost:5000`

## Database Schema

The application uses two main tables:

- `customers`: Stores customer information (id, name, email, created_at)
- `purchases`: Stores purchase records (id, product, amount, date, customer_id)

## Sample Data

The application initializes with sample data for three customers:
- John Doe
- Jane Smith
- Bob Johnson

Each customer has associated purchase records for demonstration purposes.