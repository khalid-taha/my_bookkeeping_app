#!/usr/bin/bash

# Load environment variables from .env file
export $(grep -v '^#' .env | xargs)

# Verify location of sqlite3.exe
which sqlite3.exe 

# Check sqlite3 version
sqlite3.exe --version

# Extract the file path from DATABASE_URL
DB_PATH=$(echo $DATABASE_URL | sed 's|sqlite:///||')

# Ensure the instance directory exists
mkdir -p $(dirname $DB_PATH)

# Check if the database file exists, if not, create an empty file
if [ ! -f "$DB_PATH" ]; then
    touch "$DB_PATH"
fi

# Check for reset option
RESET_DB=false
if [ "$1" == "--reset" ]; then
    RESET_DB=true
fi

# Copy ddl.sql to a temporary file
TEMP_DDL=$(mktemp)
cp ddl.sql "$TEMP_DDL"

# Uncomment drop table statements if reset option is provided
if [ "$RESET_DB" = true ]; then
    sed -i 's/-- DROP TABLE IF EXISTS/DROP TABLE IF EXISTS/' "$TEMP_DDL"
    echo "Database reset: drop statements uncommented."
fi

# Execute SQL commands from temporary ddl.sql
sqlite3.exe "$DB_PATH" < "$TEMP_DDL"
echo "Database tables created and data inserted (if not already present)."

# Clean up temporary file
rm "$TEMP_DDL"
