# FastAPI Starter Template

A reusable starter template for building Python backend applications using FastAPI.

This repository provides a clean and modular project structure with essential configurations and database integration, allowing developers to quickly initialize new backend projects.

## Features

- Modular and scalable project structure
- FastAPI application setup
- Environment-based configuration using `.env`
- SQLAlchemy database integration
- MariaDB / MySQL support
- PyMySQL database driver
- Database session management
- Pydantic Settings for application configuration
- Health check endpoints
- Environment variable example file (`.env.example`)

## Tech Stack

- **Python 3.12+**
- **FastAPI**
- **Uvicorn**
- **SQLAlchemy**
- **Pydantic**
- **Pydantic Settings**
- **MariaDB / MySQL**
- **PyMySQL**

## Project Structure

```text
project/
│
├── app/
│   ├── api/
│   ├── core/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   ├── repositories/
│   ├── utils/
│   └── main.py
│
├── storage/
│   └── uploads/
│
├── .env
├── .env.example
├── .gitignore
└── requirements.txt
```

## Getting Started

### 1. Clone the repository

```bash
git clone <repository-url>
cd <project-folder>
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

Windows CMD:

```cmd
.venv\Scripts\activate
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure environment variables

Copy `.env.example` to `.env` and configure your database credentials.

### 6. Run the application

```bash
uvicorn app.main:app --reload
```

## API Documentation

After starting the application, interactive API documentation is available at:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Environment Variables

The `.env.example` file contains the required configuration variables.

Never commit your actual `.env` file or database credentials.

## Usage

Use this repository as a starting point for new FastAPI projects. Clone or copy the template, update the application configuration, and add your project-specific models, schemas, services, repositories, and API routes.

## License

MIT License
