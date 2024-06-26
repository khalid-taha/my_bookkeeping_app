# My Bookkeeping App

## Overview

This repository contains a bookkeeping application that allows users to manage their financial data through a user-friendly web interface. The application is designed to be run from a Jupyter notebook, which initializes the web UI. The application is built using Python and Flask, with data storage and manipulation handled by various Python scripts.

## Features

- User-friendly web interface for entering and managing financial data
- Easy setup and execution from a Jupyter notebook
- Modular code structure for easy maintenance and updates

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.7 or higher
- Jupyter Notebook
- Flask
- SQLAlchemy
- Any other dependencies listed in `requirements.txt`

### Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/khalid-taha/my_bookkeeping_app.git
    cd my_bookkeeping_app
    ```

2. Install the required dependencies:

    ```sh
    pip install -r requirements.txt
    ```

### Running the Application

1. Open the Jupyter notebook `app_launcher.ipynb` in your Jupyter environment.

2. Execute the cells in the notebook. This will start the Flask server and launch the web UI.

3. Open your browser and navigate to `http://127.0.0.1:5000` to start using the application.

## Code Structure

The application is divided into several Python scripts, each handling different aspects of the bookkeeping process. Below is an overview of how these scripts interact:

### Main Components

- **app_launcher.ipynb**: The Jupyter notebook that initializes and runs the Flask server.
- **app.py**: The main Flask application file. It sets up the web server and handles routing.
- **setup_database.py**: Initializes the SQLite database and defines the data models.
- **models.py**: Contains the data models used by the application, defining the structure of the financial records (integrated with `setup_database.py`).
- **routes.py**: Defines the routes for the web application, linking URL endpoints to their corresponding functions.
- **forms.py**: Contains the forms used in the web application for data entry and validation.
- **utils.py**: Utility functions that assist with data processing and other auxiliary tasks.

### Interaction Flow

1. **Initialization**:
    - The user runs `app_launcher.ipynb`, which executes the necessary setup code to start the Flask server defined in `app.py`.

2. **Routing**:
    - `app.py` sets up the Flask application and imports routes from `routes.py`.
    - `routes.py` defines the URL endpoints and links them to the view functions that render the HTML templates or handle form submissions.

3. **Database Setup**:
    - `setup_database.py` initializes the SQLite database. It defines the `Transaction` model and includes a function `initialize_database()` to create the database and tables.

4. **Data Handling**:
    - When a user interacts with the web UI, the forms in `forms.py` are used to capture and validate input data.
    - The validated data is processed and stored using the models defined in `setup_database.py`.

5. **Utility Functions**:
    - `utils.py` provides helper functions that perform various tasks such as data formatting, calculations, and other backend operations to support the main functionality.

## Database Schema

The application uses a SQLite database to store financial records. The database schema is defined in `setup_database.py`. Below is an overview of the schema and the meaning of each column:

### Tables

#### Transaction

| Column         | Type    | Description                                  |
|----------------|---------|----------------------------------------------|
| id             | Integer | Primary key, unique identifier for each transaction |
| date           | String  | The date of the transaction (format: YYYY-MM-DD) |
| amount         | Float   | The amount of money involved in the transaction |
| category       | String  | The category to which the transaction belongs (e.g., Purchases, Sales, Purchase Returns, Sales Returns, Receipts, Payments, Petty Cash Expenses, Asset Purchases and Adjustments, Corrections and Adjustments) |
| description    | String  | A brief description of the transaction       |

### Example Data

Here is an example of how the data might look in the Transactions table:

| id | date       | amount | category                 | description                  |
|----|------------|--------|--------------------------|------------------------------|
| 1  | 2024-01-01 | 150.00 | Purchases                | Purchase of office supplies from Staples |
| 2  | 2024-01-02 | 2000.00| Sales                    | Sale of product XYZ to John Doe |
| 3  | 2024-01-03 | 75.00  | Purchase Returns         | Returned defective goods to Office Depot |
| 4  | 2024-01-04 | 150.00 | Sales Returns            | Customer return of product ABC by Jane Smith |
| 5  | 2024-01-05 | 500.00 | Receipts                 | Payment received from debtor Acme Corp. |
| 6  | 2024-01-06 | 1000.00| Payments                 | Payment to supplier Tech World |
| 7  | 2024-01-07 | 30.00  | Petty Cash Expenses      | Office snacks from local store |
| 8  | 2024-01-08 | 5000.00| Asset Purchases and Adjustments | Purchase of new computer equipment from Dell |
| 9  | 2024-01-09 | -45.00 | Corrections and Adjustments | Correction of billing error in transaction with Beta Ltd. |

## Categories Derived from Original Documents

Based on the possible original documents and books of original entry, the following categories are derived for bookkeeping purposes:

1. **Invoices from Other Firms** - Recorded in the **Purchase Day Book**
    - **Category**: Purchases

2. **Second Copy of Our Own Invoices** - Recorded in the **Sales Day Book**
    - **Category**: Sales

3. **Credit Notes from Other Firms** - Recorded in the **Purchase Returns Book**
    - **Category**: Purchase Returns

4. **Second Copy of Our Credit Notes** - Recorded in the **Sales Returns Book**
    - **Category**: Sales Returns

5. **Our Statements Record with Thanks and Cheques from Debtors** - Recorded in the **Cash Book**
    - **Category**: Receipts

6. **Statements from Our Creditors and Our Cheques** - Recorded in the **Cash Book**
    - **Category**: Payments

7. **Petty Cash Vouchers** - Recorded in the **Petty Cash Book**
    - **Category**: Petty Cash Expenses

8. **Invoices for Assets Bought and Bankruptcy Notices** - Recorded in the **Journal Proper**
    - **Category**: Asset Purchases and Adjustments

9. **Letters About Errors** - Recorded in the **Journal Proper**
    - **Category**: Corrections and Adjustments

## Contributing

We welcome contributions to enhance the functionality of this application. To contribute, please fork the repository, make your changes, and submit a pull request. Ensure your code follows the existing style and passes all tests.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgments

- Special thanks to all contributors and users who provided feedback and suggestions.

