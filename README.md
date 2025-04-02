# ATM-Interface-Using-Flask-Frame-Work

## Overview
This project is an ATM interface built using the Flask framework. It allows users to perform basic banking operations such as balance inquiry, cash withdrawal, deposit, and transaction history tracking.

## Features
- User authentication (Login & Logout)
- Check account balance
- Deposit money
- Withdraw money
- View transaction history
- Secure and session-based transactions

## Technologies Used
- Python (Flask)
- HTML, CSS (for frontend)
- SQLite (Database)
- Jinja2 (Template rendering)

## Installation & Setup

1. **Clone the Repository**
   ```sh
   git clone https://github.com/yourusername/atm-interface-flask.git
   cd atm-interface-flask
   ```

2. **Create a Virtual Environment**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Set Up the Database**
   ```sh
   python setup_db.py
   ```

5. **Run the Application**
   ```sh
   python app.py
   ```

6. **Access the Application**
   Open a web browser and visit `http://127.0.0.1:5000/`

## Project Structure
```
ATM-Interface-Flask/
│-- app.py
│-- setup_db.py
│-- templates/
│   │-- index.html
│   │-- login.html
│   │-- dashboard.html
│-- static/
│   │-- styles.css
│-- models.py
│-- requirements.txt
│-- README.md
```

## API Endpoints
| Route            | Method | Description         |
|-----------------|--------|---------------------|
| `/`             | GET    | Home Page          |
| `/login`        | GET/POST | User Login       |
| `/logout`       | GET    | User Logout        |
| `/dashboard`    | GET    | User Dashboard     |
| `/deposit`      | POST   | Deposit Money      |
| `/withdraw`     | POST   | Withdraw Money     |
| `/balance`      | GET    | Check Balance      |
| `/history`      | GET    | View Transactions  |

