# Task Management API

A RESTful API built with FastAPI for managing tasks, featuring PostgreSQL database integration and Docker containerization.

## Project Description

This project is a complete task management system featuring task lists. Users can create, read, update, and delete both lists and tasks, managing their tasks however they want. It includes full CRUD operations with data validation and database persistence.

### Technology Stack

- **FastAPI**: web framework for building APIs
- **PostgreSQL**: Relational database
- **SQLAlchemy**: Python SQL toolkit and ORM
- **Alembic**: Database migration tool
- **Pydantic**: Data validation using Python type annotations
- **Docker**: Containerization platform
- **Docker Compose**: Multi-container Docker application management

## Local Environment Setup

### Prerequisites

- Python 3.12 or higher
- PostgreSQL 15
- Git

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```

2. **Create and activate virtual environment**  
   On Linux/macOS:
   ```bash
   python -m venv env
   source env/bin/activate
   ```
   On Windows:
   ```bash
   python -m venv env
   env\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
    ### Environment Variables

    The application requires the following environment variables for database configuration:

    - `POSTGRES_USER`: Database username  
    - `POSTGRES_PASSWORD`: Database password  
    - `POSTGRES_DB`: Database name  
    - `DATABASE_URL`: Local database connection string  
    - `DOCKER_DATABASE_URL`: Docker database connection string  
    - `TEST_DATABASE_URL`: Test database connection string  

    To set these up, create a `.env` file in the root directory based on the `.env.example` template:

    ```env
    # .env.example
    POSTGRES_USER=your_username
    POSTGRES_PASSWORD=your_password
    POSTGRES_DB=your_database
    DATABASE_URL=postgresql://your_username:your_password@localhost:5432/your_database
    DOCKER_DATABASE_URL=postgresql://your_username:your_password@db:5432/your_database
    TEST_DATABASE_URL=postgresql://your_username:your_password@localhost:5432/your_test_database
    ```

5. **Set up local database**
   
   Make sure PostgreSQL is running and create the database:
   ```sql
   CREATE DATABASE tasks_db;
   ```

6. **Run database migrations**
   ```bash
   alembic upgrade head
   ```

7. **Start the application**
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```

The API will be available at `http://localhost:8000`


## Running with Docker

### Prerequisites

- Docker
- Docker Compose

### Docker Setup

1. **Build and start containers**
   ```bash
   docker-compose up --build
   ```

2. **Run in detached mode**
   ```bash
   docker-compose up -d
   ```

3. **View logs**
   ```bash
   docker-compose logs -f
   ```

4. **Stop containers**
   ```bash
   docker-compose down
   ```

### Container Information

- **Backend**: Runs on port 8000
- **Database**: PostgreSQL on port 5432
- **Auto-reload**: Enabled for development

The application automatically runs database migrations on startup when using Docker.

## API Documentation

Once the application is running, you can access:

- **Interactive API docs**: `http://localhost:8000/docs`
