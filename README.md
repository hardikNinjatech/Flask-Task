# Event Fetcher Application

This is a Flask application that fetches events from an external XML-based API and stores them in a database.



## Prerequisites
- Python 3.6+
- pip
- virtualenv (optional, but recommended)
- Flask
- SQLAlchemy
- postgreSQL

## Installation

### 1. Create Database
 - First, create a database in PostgreSQL:
CREATE DATABASE your_database_name;

### 2. Create .env File 
 - Create a .env file in the root of your project directory and add the following line, replacing <username>, <password>, <hostname>, and <database_name> with your actual database credentials:

```SQLALCHEMY_DATABASE_URI=postgresql://<username>:<password>@<hostname> <database_name>```

### 3. Create Virtual Environment
 - Create a virtual environment for your project:
`python -m venv .venv`

### 4. Activate Virtual Environment
 - Activate the virtual environment.
 
 - On Windows:

```sh
.venv\Scripts\activate
```

- On Unix or MacOS:

``` sh
source .venv/bin/activate
```

### 5. Install Requirements
 - Install the required Python packages using the requirements.txt file:

 ``` sh
pip install -r requirements.txt
```


### 6. Run Migrations
 - Run the migrations to set up your database schema:
``` sh
make migrate
```

### 7. Run the Application
 - Finally, run the application:
 ``` sh
make run
```
Application will run on 
``` sh
http://127.0.0.1:5000
```

### 8. Api Endpoint

``` sh
{base_url}/events?starts_at=1625086800&ends_at=1627765200
```

NOTE :- provide timestamp in params

## Additional Information
Ensure that PostgreSQL is running and accessible.
Adjust any other configurations in the .env file as needed.
