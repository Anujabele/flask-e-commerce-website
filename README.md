# market_flask
# 🛒 Flask Market App

A full-featured Flask web application where users can register, log in, and interact with a virtual marketplace. They can buy items within their budget, sell owned items back to the market, and use advanced filters to search or sort the available items.


## 🚀 Features

- 🧑‍💼 User Registration & Login
- 🔐 Secure authentication with Flask-Login and Bcrypt
- 💰 User Budget Management
- 🛍 Buy & Sell Items
- 🔍 **Search & Filter Options:**
  - Search by item name
  - Sort by price (Low to High, High to Low)
  - Show only affordable items based on user's budget
- ⚙️ Built using Flask, SQLAlchemy, WTForms, and Bootstrap
- 🎯 Flash messages for user feedback

## Tech Stacks
  - Python 3
  - Flask
  - Flask-WTF
  - Flask-Login
  - Flask-Bcrypt
  - SQLAlchemy(with SQLite)
  - Bootstrap 4
  - Jinja2

## Setup Instructions
-Clone the Repository
git clone https://github.com/Anujabele/flask-e-commerce-website.git
cd flask-e-commerce-website

-Install Dependencies
python -m venv venv
# Activate the environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt

-Database Setup
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

-Running the app
flask run






