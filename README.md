# Event Fetcher Application

This is a Flask application that fetches events from an external XML-based API and stores them in a database.



## Prerequisites
- Python 3.6+
- pip
- virtualenv (optional, but recommended)
- Flask
- SQLAlchemy

## Installation

1. Create Database
 - First, create a database in PostgreSQL:
CREATE DATABASE your_database_name;

2. Create .env File
 - Create a .env file in the root of your project directory and add the following line, replacing <username>, <password>, <hostname>, and <database_name> with your actual database credentials:

`SQLALCHEMY_DATABASE_URI=postgresql://<username>:<password>@<hostname> <database_name>`

3. Create Virtual Environment
 - Create a virtual environment for your project:
`python -m venv .venv`

4. Activate Virtual Environment
 - Activate the virtual environment.
 
    - On Windows:

`.venv\Scripts\activate`

- On Unix or MacOS:

`source .venv/bin/activate`

5. Install Requirements
 - Install the required Python packages using the requirements.txt file:
`pip install -r requirements.txt`

6. Run Migrations
 - Run the migrations to set up your database schema:
`make migrate`

7. Run the Application
 - Finally, run the application:
`make run`

## Additional Information
Ensure that PostgreSQL is running and accessible.
Adjust any other configurations in the .env file as needed.
