-- Table DDL for transactions
-- CREATE TABLE transactions (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     transaction_date DATE NOT NULL,  -- Changed to DATE
--     total_amount DOUBLE NOT NULL,
--     amount DOUBLE NOT NULL,
--     vat DOUBLE NOT NULL,
--     transaction_description TEXT,
--     category_id INTEGER,
--     FOREIGN KEY (category_id) REFERENCES categories(id)
-- )

INSERT INTO transactions (id, transaction_date, total_amount, amount, vat, transaction_description, category_id) VALUES (1, '2024-06-01', 118.8, 108.0, 10.8, 'R Brown & Co', 1);
INSERT INTO transactions (id, transaction_date, total_amount, amount, vat, transaction_description, category_id) VALUES (2, '2024-06-17', 480.48, 436.8, 43.68, 'Peter Young Ltd', 1);
INSERT INTO transactions (id, transaction_date, total_amount, amount, vat, transaction_description, category_id) VALUES (3, '2024-06-21', 65.34, 59.4, 5.94, 'Ambrose Smith Ltd', 1);
INSERT INTO transactions (id, transaction_date, total_amount, amount, vat, transaction_description, category_id) VALUES (4, '2024-06-30', 414.48, 376.8, 37.68, 'Major & Co Ltd', 1);
