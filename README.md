# WowPatterns

A full-stack e-commerce application migrated from a legacy PHP/CodeIgniter application to a modern **FastAPI + React + TypeScript** architecture.

The project manages customers, products, categories, shopping bags, orders, payments, and related e-commerce functionality.

## Tech Stack

### Backend

* Python
* FastAPI
* SQLAlchemy
* MariaDB
* Pydantic
* JWT authentication
* Password hashing
* Razorpay payment integration
* Razorpay webhooks

### Frontend

* React
* TypeScript
* Vite
* React Router
* CSS

### Development Tools

* Git
* GitHub
* Swagger / OpenAPI
* Virtual environment (`venv`)

## Project Structure

```text
wowpatterns/
│
├── app/
│   ├── core/
│   │   ├── config.py
│   │   ├── database.py
│   │   ├── security.py
│   │   ├── razorpay.py
│   │   └── code_generator.py
│   │
│   ├── models/
│   ├── repositories/
│   ├── routers/
│   ├── schemas/
│   ├── services/
│   └── main.py
│
├── frontend/
│   └── src/
│       ├── components/
│       ├── pages/
│       ├── services/
│       ├── types/
│       └── ...
│
├── requirements.txt
├── .gitignore
└── README.md
```

## Backend Architecture

The FastAPI backend follows a layered structure:

```text
Router
   ↓
Service
   ↓
Repository
   ↓
SQLAlchemy Model
   ↓
MariaDB
```

This separation keeps API endpoints, business logic, database operations, and data models organized independently.

## Implemented Backend Areas

The backend contains APIs and supporting layers for:

* Customer registration and login
* JWT authentication
* Customer profile
* Customer addresses
* Customer downloads
* Products
* Product categories
* Product category types
* Product specifications
* Product images
* Product design specifications
* Shopping bag
* Orders
* Order items
* Shipping status
* Shipping prices
* Inquiries
* Design file types
* Razorpay payments
* Razorpay failed-payment events
* Razorpay webhooks

## Authentication

Customer authentication uses JWT-based authentication.

The application supports:

* Customer registration
* Password hashing
* Login
* Access-token generation
* Protected API endpoints
* Current-customer retrieval
* Customer profile updates

Protected requests use the standard Bearer token format:

```text
Authorization: Bearer <access_token>
```

## Product APIs

Product functionality includes operations for:

* Product listing
* Product details
* Product creation
* Product updates
* Product activation/deactivation
* Product-related information

The API is documented through FastAPI's automatically generated Swagger/OpenAPI interface.

## Payment Integration

The application includes Razorpay payment integration and supporting webhook/payment-event handling.

Payment-related backend components include:

* Payment creation
* Payment service
* Razorpay configuration
* Failed payment event handling
* Razorpay webhook handling

Sensitive credentials are stored outside the source code using environment variables.

## Frontend

The React frontend currently includes:

* Home page
* Login
* Customer profile
* Protected routes
* Navigation/layout
* Product listing
* Product details

The frontend communicates with the FastAPI backend through API service modules.

## Running the Backend

Create and activate a Python virtual environment:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file containing the required local configuration.

Start FastAPI:

```bash
uvicorn app.main:app --reload
```

The API will normally be available at:

```text
http://localhost:8000
```

Swagger documentation:

```text
http://localhost:8000/docs
```

## Running the Frontend

Go to the frontend directory:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the Vite development server:

```bash
npm run dev
```

The frontend will normally be available at the URL displayed by Vite.

The frontend uses the following environment variable for the backend API:

```text
VITE_API_URL=http://localhost:8000
```

## Environment Variables

Secrets and environment-specific configuration should be stored in `.env`.

Example:

```text
DATABASE_URL=...
SECRET_KEY=...
RAZORPAY_KEY_ID=...
RAZORPAY_KEY_SECRET=...
```

Actual credentials should never be committed to GitHub.

## API Documentation

Once the FastAPI server is running, interactive API documentation is available at:

```text
http://localhost:8000/docs
```

The Swagger interface can be used to test and inspect the available APIs.

## Migration Project

WowPatterns is also a practical migration project.

The original application was developed using a legacy PHP/CodeIgniter architecture. This project modernizes the backend using Python and FastAPI while introducing a React + TypeScript frontend.

The migration provides practical experience with:

* Legacy application analysis
* Database/table mapping
* REST API development
* Layered backend architecture
* Authentication
* Payment integration
* React frontend development
* API integration
* Git/GitHub workflow

## Current Status

The core backend API structure and major e-commerce API areas have been implemented.

The React frontend currently includes authentication, protected navigation, customer profile functionality, product listing, and product details.

Further production-oriented improvements can include additional frontend workflows, automated testing, containerization, deployment, and cloud configuration.

## Author

**Suhasini**

Full Stack Developer — Python / FastAPI / React
