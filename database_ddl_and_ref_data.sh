#!/usr/bin/bash

# Verify location of sqlite3.exe
which sqlite3.exe 

# Check sqlite3 version
sqlite3.exe --version

# Path to your SQLite database
DB_PATH='./instance/my_database.db'

# Check if the database file exists, if not, create an empty file
if [ ! -f "$DB_PATH" ]; then
    touch "$DB_PATH"
fi

# SQL commands to execute
SQL_COMMANDS=$(cat <<EOF
-- Drop transactions table if it exists
DROP TABLE IF EXISTS transactions;

-- Drop categories table if it exists
DROP TABLE IF EXISTS categories;

-- Create categories table
CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);

-- Create transactions table
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    total_amount DOUBLE NOT NULL,  -- Changed
    amount DOUBLE NOT NULL,  -- Changed
    vat DOUBLE NOT NULL,  -- Changed
    transaction_description TEXT,  -- Changed
    category_id INTEGER,
    FOREIGN KEY (category_id) REFERENCES categories(id)
);

-- Populate categories table
INSERT INTO categories (name) VALUES ('Purchases');
INSERT INTO categories (name) VALUES ('Sales');
INSERT INTO categories (name) VALUES ('Purchase Returns');
INSERT INTO categories (name) VALUES ('Sales Returns');
INSERT INTO categories (name) VALUES ('Receipts');
INSERT INTO categories (name) VALUES ('Payments');
INSERT INTO categories (name) VALUES ('Petty Cash Expenses');
INSERT INTO categories (name) VALUES ('Asset Purchases and Adjustments');
INSERT INTO categories (name) VALUES ('Corrections and Adjustments');

SELECT * FROM categories;
EOF
)

# Execute SQL commands
echo "$SQL_COMMANDS" | sqlite3.exe "$DB_PATH"
