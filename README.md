# Steptech Assignment

## Overview

Welcome to the Steptech Assignment project! This Flask application is designed to manage user data using a MySQL database. It features APIs, routing, and a clean UI to make your development experience seamless.

## Setup and Running

### Prerequisites

- Python 3.x
- Flask (`pip install Flask`)
- MySQL Database Server
- Visual Studio Code (VS Code)

### Getting Started

1. **Clone the Repository:**
   ```bash
   
   git clone https://github.com/your-username/steptech_assignment.git
   cd steptech_assignment
# setup virtual envirnoment 
python -m venv venv
source venv/bin/activate   # For Linux/Mac
.\venv\Scripts\activate    # For Windows

#Install Dependencies:
pip install -r requirements.txt
#Configure MySQL:
 Create a database named steptechdb.
Update the db_config in app.py with your database credentials.
#Run the Application:
python app.py
flask run

Access the Application:
Visit http://localhost:5000 in your web browser.

Populating Database
Insert sample data into the new_table table:
INSERT INTO users (name, email, password, role) VALUES
('John Doe', 'john@example.com', 'password123', 'admin'),
('Jane Smith', 'jane@example.com', 'pass456', 'user'),
('Bob Johnson', 'bob@example.com', 'bobpass', 'user');


Git Workflow
1) Fork the Repository.
2) Clone Your Fork:
bash : git clone https://github.com/your-username/steptech_assignment.git
Create a New Branch: git checkout -b feature-branch
Make Changes, Commit, and Push: git add .
git commit -m "Your commit message"
git push origin feature-branch
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Steptech Assignment - SQL Setup

## Overview

This section provides information on setting up the MySQL database for the Steptech Assignment project.

## Database Schema

The application uses a table named `users` with the following schema:

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(50) NOT NULL
);
Setting Up the Database
Follow the steps below to set up the MySQL database and populate it with sample data.

Prerequisites
MySQL Database Server installed.
Access to MySQL Workbench or any MySQL client.
Steps
Create a Database:

sql
Copy code
CREATE DATABASE steptechdb;
Use the Database:

sql
Copy code
USE steptechdb;
Create the users Table:

sql
Copy code
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(50) NOT NULL
);
Insert Sample Data:

sql
Copy code
INSERT INTO users (name, email, password, role) VALUES
('John Doe', 'john@example.com', 'password123', 'admin'),
('Jane Smith', 'jane@example.com', 'pass456', 'user'),
('Bob Johnson', 'bob@example.com', 'bobpass', 'user');
Connecting Flask to MySQL
In your Flask application (app.py), ensure the db_config dictionary reflects your MySQL server details:

python
Copy code
db_config = {
    'host': 'localhost',
    'user': 'your_username',
    'password': 'your_password',
    'database': 'steptechdb'
}
Make sure to replace 'your_username' and 'your_password' with your actual MySQL credentials.

Running the Application
After setting up the database, follow the instructions in the main README file to run your Flask application.

sql
Copy code


Feel free to customize the information based on your specific database setup and requirements.
