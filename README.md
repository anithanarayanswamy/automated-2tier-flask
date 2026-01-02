# Two-Tier Customer Sales Application (Flask + MySQL)

## Overview

This project is a **production-style two-tier web application** designed to allow a client to view **customer sales and purchase details by customer name**.

The system exposes a RESTful backend built with **Flask**, backed by a **MySQL database**, fully containerized using **Docker**.

The project is intentionally designed to demonstrate **real-world DevOps practices**, clean architecture, and deployment-ready patterns rather than just application logic.

---

## Business Use Case

The client wants a system where:

* Customer purchase records are stored centrally
* A user can query sales data by entering a customer name
* The backend returns structured purchase details
* The system can scale and be deployed reliably
* Monitoring and automation are built in

This mirrors common enterprise use cases such as:

* Sales dashboards
* CRM backend services
* Order lookup services
* Internal reporting APIs

---

## Technology Stack

### Application

* **Python 3**
* **Flask** – REST API framework
* **SQLAlchemy** – ORM for database access
* **PyMySQL** – MySQL database connector
* **cryptography** – Security library for MySQL authentication

### DevOps / Infrastructure

* **Docker** – Containerization
* **Docker Compose** – Multi-service orchestration
* **MySQL 8** – Relational database

---

## Project Structure

```
.
├── app/
│   ├── __init__.py          # Flask app factory
│   ├── routes/              # API routes (controllers)
│   │   ├── health.py        # Health check endpoint
│   │   ├── customers.py     # Customer data endpoint
│   │   └── main.py          # Root endpoint
│   ├── services/            # Business logic layer
│   │   └── customer_service.py
│   ├── models/              # Database models
│   │   └── customer.py
│   └── config/              # Configuration
│       └── settings.py
├── scripts/                 # Initialization scripts
│   └── populate_db.py       # Script to populate sample data
├── run.py                   # Application entry point
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables
├── Dockerfile               # Docker configuration
└── docker-compose.yml       # Multi-container orchestration
```

---

## Application Design Principles

### Layered Architecture

The application follows strict separation of concerns:

| Layer    | Responsibility                   |
| -------- | -------------------------------- |
| Routes   | Handle HTTP requests & responses |
| Services | Business logic & validation      |
| Models   | Database schema & queries        |
| Config   | Environment-based configuration  |

This structure improves:

* Maintainability
* Testability
* Scalability
* CI/CD compatibility

---

## API Design

### Root Endpoint

Provides information about the API:

```
GET /
```

Response:

```json
{
  "message": "Welcome to the Two-Tier Customer Sales Application",
  "endpoints": {
    "health": "/health",
    "customers": "/customers?name=<customer_name>"
  },
  "description": "This is a production-style two-tier web application designed to allow a client to view customer sales and purchase details by customer name."
}
```

### Health Check Endpoint

Used for:

* Docker health checks
* Load balancers
* Monitoring
* CI validation

```
GET /health
```

Response:

```json
{
  "status": "ok"
}
```

---

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
    },
    {
      "product": "Mouse",
      "amount": 25.99,
      "date": "2024-01-20"
    }
  ]
}
```

---

## Configuration Management

The application uses **environment variables** instead of hardcoded values.

### Example configuration variables:

```
FLASK_APP=run.py
FLASK_ENV=development
FLASK_DEBUG=true
DATABASE_URL=mysql+pymysql://root:password@db:3306/customerdb
SECRET_KEY=your-super-secret-key-change-in-production
PORT=5000
```

### Why environment-based configuration?

* Works across local, Docker, CI, and AWS
* Prevents secrets from being committed
* Enables easy promotion across environments
* Industry-standard DevOps practice

---

## Local Development Workflow

### 1. Clone the repository

```bash
git clone <repo-url>
cd automated-2tier-flask
```

### 2. Install dependencies (if running locally without Docker):

```bash
pip install -r requirements.txt
```

### 3. Set up environment variables:

```bash
cp .env .env
```

Application runs at:

```
http://localhost:5000
```

---

## Docker Workflow

### Why Docker?

* Ensures consistency across environments
* Eliminates “works on my machine” issues
* Required for CI/CD and cloud deployment

### Docker usage (high-level)

* Flask app runs inside a container
* MySQL runs in a separate container
* Docker Compose orchestrates both
* Environment variables injected at runtime

### Running with Docker Compose

```bash
# Build and start containers
docker-compose up --build

# Or run in detached mode
docker-compose up -d

# Stop containers
docker-compose down
```

### Populate database with sample data

```bash
# After containers are running, populate with sample data
docker exec -e PYTHONPATH=/app -w /app automated-2tier-flask-app-1 python3 scripts/populate_db.py
```

---

## Database Schema

The application uses two main tables:

- `customers`: Stores customer information (id, name, email, created_at)
- `purchases`: Stores purchase records (id, product, amount, date, customer_id)

---

## Sample Data

The application is populated with **10 sample customers** and their purchase records:

1. **John Doe** - 3 purchases
2. **Jane Smith** - 2 purchases
3. **Bob Johnson** - 1 purchase
4. **Alice Williams** - 2 purchases
5. **Charlie Brown** - 3 purchases
6. **Diana Miller** - 3 purchases
7. **Ethan Davis** - 2 purchases
8. **Fiona Garcia** - 3 purchases
9. **George Rodriguez** - 2 purchases
10. **Helen Martinez** - 4 purchases

Total: **25 purchase records** across 10 customers

---

## Security Considerations

* No secrets committed to Git
* Environment variables used for credentials
* MySQL protected behind private network
* Principle of least privilege for DB users
* Root access avoided in production
* Container isolation enabled

---

## Future Enhancements

* Authentication & authorization
* Pagination & filtering
* API versioning
* Swagger/OpenAPI documentation
* Database migrations (Alembic)
* Kubernetes deployment
* Metrics with Prometheus
* Alerting via CloudWatch
* Frontend UI
* Role-based access control

---

## Project Goals

This project demonstrates:

✅ Backend API design
✅ Database integration (MySQL)
✅ Clean architecture
✅ Dockerized application with multiple services
✅ Environment-based configuration
✅ Sample data initialization (10 customers with 25 purchases)
✅ Monitoring readiness
✅ Production-level DevOps thinking

---