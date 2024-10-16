# Flask OpenAI Q&A Application

## Overview

This project is a Flask-based web application that allows users to ask questions and receive answers generated by the OpenAI API.
It uses a PostgreSQL database to store the questions and answers and leverages Alembic for database migrations.
The application is tested using pytest.

## Features

- Accepts questions via a RESTful API.
- Integrates with the OpenAI API to generate answers.
- Stores questions and answers in a PostgreSQL database.
- Manages database schema changes using Alembic.
- Includes unit tests using pytest to ensure functionality.

## Technologies Used

- **Flask**: Web framework for building the API.
- **Flask-SQLAlchemy**: ORM for database interactions.
- **PostgreSQL**: Database for storing questions and answers.
- **Alembic**: Migration tool for handling database schema changes.
- **OpenAI API**: Provides AI-generated answers to questions.
- **pytest**: Testing framework for unit tests.

## Directory Structure

**/app**

  |─ app.py : Main application file
    
  |─ dal.py : Data access layer for database interactions

  |─ models.py : Database models

  |─ openai_integration.py : Integration with OpenAI API
    
**/tests**

  |─ test_app.py : Unit tests for the application
    
/alembic : Alembic migration scripts

  |─ env.py # environment file for alembic
    
  |─ /versions # alembic version scripts

alembic.ini : Alembic configuration file 

Dockerfile # Dockerfile for the Flask application
docker-compose.yml # Docker Compose configuration - PostgreSQL Offical image was used 
requirements.txt # Project dependencies

## Setup Instructions

### Installation

1- Clone the repository:

```bash
git clone <repository_url>
cd assignment_insaitai
docker-compose up --build
```
2- Database Migrations
  To create and apply migrations with Alembic:
 ```bash
 alembic init alembic
 ```
  Create a new migration:
  ```bash
  alembic revision --autogenerate -m "Initial migration"
 ```
  Apply the migration:
```bash
alembic upgrade head
```

3- Running Tests
  To run the tests using pytest:
```bash
pytest
```

## API Usage
# Ask a Question
  - Endpoint: /ask
      - example with curl :
        ```
        curl  --location 'localhost:5000/ask' \
        --header 'Content-Type: application/json' \
        --data '{
        "question": "how are you?"
        }'
        ```
  - Method: POST
Request Body:
```
{
    "question": "Your question here"
}
```
Response:
```
{
    "question": "Your question here",
    "answer": "Generated answer from OpenAI"
}
```
