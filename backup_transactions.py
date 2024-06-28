import sqlite3
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the database URL from environment variables
db_path = os.getenv('DATABASE_URL')
if db_path and db_path.startswith('sqlite:///'):
    db_path = db_path.replace('sqlite:///', '')

# Define the output file for the backup SQL statements
backup_file = 'backup_transactions.sql'

# Connect to the SQLite database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Get the DDL for the transactions table
cursor.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name='transactions'")
table_ddl = cursor.fetchone()[0]

# Query the transactions table
cursor.execute("SELECT * FROM transactions")
transactions = cursor.fetchall()

# Get the column names from the transactions table
column_names = [description[0] for description in cursor.description]

# Open the backup file for writing
with open(backup_file, 'w') as f:
    # Write the table DDL as a comment
    f.write("-- Table DDL for transactions\n")
    for line in table_ddl.splitlines():
        f.write(f"-- {line}\n")
    f.write("\n")

    # Write the insert statements
    for transaction in transactions:
        # Construct the INSERT statement
        insert_statement = f"INSERT INTO transactions ({', '.join(column_names)}) VALUES ({', '.join(['?' for _ in transaction])});\n"
        # Format the statement with the transaction values, enclosing dates and strings in quotes
        insert_statement = insert_statement.replace('?', '{}').format(
            *[f"'{value}'" if isinstance(value, str) or isinstance(value, sqlite3.Date) else value for value in transaction]
        )
        # Write the statement to the backup file
        f.write(insert_statement)

# Close the database connection
conn.close()

print(f"Backup completed. The INSERT statements have been written to {backup_file}.")
