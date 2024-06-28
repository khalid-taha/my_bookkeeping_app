# Book Keeping System

## Overview

This is a Flask-based web application designed for book-keeping. Users can create, edit, delete, and view transactions categorized into different types. The system uses SQLAlchemy for database interactions and SQLite as the database backend.

## Table of Contents

- [Book Keeping System](#book-keeping-system)
  - [Overview](#overview)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Project Structure](#project-structure)
  - [Configuration](#configuration)
  - [Database Initialization](#database-initialization)
  - [Contributing](#contributing)
  - [License](#license)

## Features

- Create, edit, and delete transactions
- Categorize transactions into predefined categories
- View a list of all transactions
- Simple and intuitive user interface

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/transaction-management-system.git
    cd transaction-management-system
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database**:
    ```bash
    bash database_ddl_and_ref_data.sh
    ```

## Usage

1. **Run the Flask application**:
    ```bash
    python app.py
    ```

2. **Open your web browser** and navigate to `http://127.0.0.1:5000/`

## Project Structure

```
transaction-management-system/
│
├── app.py
├── config.py
├── db_config.py
├── forms.py
├── models.py
├── concat_py_files.sh
├── database_ddl_and_ref_data.sh
├── initialize_database.ipynb
│
├── templates/
│   ├── edit_transaction.html
│   ├── new_transaction.html
│   ├── transactions.html
│
├── requirements.txt
└── README.md
```

## Configuration

Configuration settings are located in `config.py`:
```python
class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///my_database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```

## Database Initialization

The `database_ddl_and_ref_data.sh` script sets up the SQLite database:
- Creates an empty database file if it does not exist
- Creates necessary tables (`categories` and `transactions`)
- Populates the `categories` table with predefined values

Run the script:
```bash
bash database_ddl_and_ref_data.sh
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.