# Student Database Management System

A backend API for managing student information using FastAPI, SQLite, and SQLAlchemy.

## Features

- FastAPI backend
- SQLite database
- SQLAlchemy ORM
- Student management API
- REST API structure
- Interactive Swagger API documentation
- Modular project structure

## Technologies Used

- Python
- FastAPI
- Uvicorn
- SQLite
- SQLAlchemy
- Pydantic

## Project Structure

```text
student_database_ai/
│
├── app/
│   ├── main.py
│   │
│   ├── database/
│   │   ├── __init__.py
│   │   └── database.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   └── student.py
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── student.py
│   │
│   └── routes/
│       ├── __init__.py
│       └── students.py
│
├── requirements.txt
├── .gitignore
└── README.md
