-- Uncomment the following lines to drop existing tables
-- DROP TABLE IF EXISTS transactions;
-- DROP TABLE IF EXISTS categories;

-- Create categories table
CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);

-- Create transactions table
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    transaction_date DATE NOT NULL,  -- Changed to DATE
    total_amount DOUBLE NOT NULL,
    amount DOUBLE NOT NULL,
    vat DOUBLE NOT NULL,
    transaction_description TEXT,
    category_id INTEGER,
    FOREIGN KEY (category_id) REFERENCES categories(id)
);

-- Insert initial data if the categories table is empty
INSERT OR IGNORE INTO categories (id, name) VALUES 
(1, 'Purchases'),
(2, 'Sales'),
(3, 'Purchase Returns'),
(4, 'Sales Returns'),
(5, 'Receipts'),
(6, 'Payments'),
(7, 'Petty Cash Expenses'),
(8, 'Asset Purchases and Adjustments'),
(9, 'Corrections and Adjustments');

SELECT * FROM categories;
