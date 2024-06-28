# High-Level Documentation for Book-Keeping System

## Overview

This document provides a high-level overview of the book-keeping system implemented using Flask, SQLAlchemy, and SQLite. The system allows users to create, edit, delete, and list financial transactions categorized into different types.

## Components

### 1. **Flask Application (app.py)**
   - **Purpose**: Acts as the main entry point for the web application.
   - **Key Functionalities**:
     - Initializes the Flask app and configures it with settings from `config.py`.
     - Defines routes for creating, editing, deleting, and listing transactions.
     - Utilizes SQLAlchemy for ORM (Object Relational Mapping) to interact with the SQLite database.
   - **Endpoints**:
     - `/`: Redirects to the list of transactions.
     - `/new_transaction`: Displays a form to create a new transaction and handles form submissions.
     - `/edit_transaction/<int:id>`: Displays a form to edit an existing transaction and handles form submissions.
     - `/delete_transaction/<int:id>`: Handles the deletion of a transaction.
     - `/transactions`: Displays a list of all transactions.

### 2. **Configuration (config.py)**
   - **Purpose**: Provides configuration settings for the Flask application.
   - **Key Settings**:
     - `SQLALCHEMY_DATABASE_URI`: Specifies the path to the SQLite database file.
     - `SQLALCHEMY_TRACK_MODIFICATIONS`: Disables modification tracking to save resources.

### 3. **Database Configuration (db_config.py)**
   - **Purpose**: Initializes and configures the SQLAlchemy instance.
   - **Key Components**:
     - `db`: An instance of `SQLAlchemy` used for database operations.

### 4. **Database Models (models.py)**
   - **Purpose**: Defines the schema for the database tables.
   - **Key Models**:
     - **Category**:
       - Represents transaction categories.
       - Fields: `id`, `name`.
     - **Transaction**:
       - Represents financial transactions.
       - Fields: `id`, `total_amount`, `amount`, `vat`, `transaction_description`, `category_id`.
       - Relationships: Each transaction belongs to a category.

### 5. **Forms (forms.py)**
   - **Purpose**: Defines the form structure for creating and editing transactions.
   - **Key Components**:
     - **TransactionForm**:
       - Fields: `category` (SelectField with categories as choices), other transaction-specific fields.

### 6. **Shell Script for Concatenation (concat_py_files.sh)**
   - **Purpose**: Concatenates various code files into a single file for easier review and management.
   - **Functionality**: Loops through specified file types, appending their contents to a single output file (`code.txt`).

### 7. **Database Initialization Script (database_ddl_and_ref_data.sh)**
   - **Purpose**: Sets up the SQLite database by creating necessary tables and inserting reference data.
   - **Key Actions**:
     - Creates an empty database file if it does not exist.
     - Executes SQL commands to drop existing tables and create new ones.
     - Inserts predefined categories into the `categories` table.

### 8. **Jupyter Notebook for Database Initialization (initialize_database.ipynb)**
   - **Purpose**: Provides a step-by-step guide to initialize and verify the database setup.
   - **Key Steps**:
     - Runs the database initialization shell script.
     - Connects to the SQLite database and verifies table contents.
     - Runs the Flask application in the background for testing.
     - Opens a browser window to display the transactions.
     - Terminates Flask instances to clean up the environment.

### 9. **HTML Templates**
   - **Purpose**: Provides the user interface for interacting with the application.
   - **Key Templates**:
     - **edit_transaction.html**: Form for editing a transaction.
     - **new_transaction.html**: Form for creating a new transaction.
     - **transactions.html**: Displays a list of transactions with options to edit or delete each.

## System Workflow

1. **Initialization**:
   - The database is initialized using `database_ddl_and_ref_data.sh`, creating the necessary tables and populating reference data.

2. **Application Startup**:
   - The Flask application (`app.py`) is started, loading configuration settings from `config.py`.

3. **User Interaction**:
   - Users interact with the application through web forms (`new_transaction.html`, `edit_transaction.html`) to manage transactions.
   - Transactions are listed on the `transactions.html` page, where users can edit or delete entries.

4. **Database Operations**:
   - SQLAlchemy is used to perform CRUD operations on the database, ensuring data integrity and consistency.

5. **Form Handling**:
   - Forms are handled by `FlaskForm` from `flask_wtf`, with data validation and submission logic implemented in the route handlers.

6. **Code Management**:
   - Code files are concatenated using `concat_py_files.sh` for easier management and review.

7. **Testing and Verification**:
   - Database initialization and verification are performed in `initialize_database.ipynb`.

## Conclusion

This system provides a robust framework for managing financial transactions using a combination of Flask for the web application, SQLAlchemy for ORM, and SQLite for the database. The modular structure ensures ease of maintenance, scalability, and flexibility for future enhancements.