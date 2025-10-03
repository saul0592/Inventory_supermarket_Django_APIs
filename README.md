# Inventory_supermarket_Django_APIs

This project is a supermarket inventory management system built with **Django**.  
It provides APIs to handle product data and an initial interface with HTML login functionality.  

---

## Features (current progress)
- Django project structure ready for development  
- Basic API setup for inventory management  
- Initial login interface in HTML  
- Ready to be extended with more CRUD operations and user authentication  

---

## 📂 Project Structure
inventory_Apis/
├── inventory/ # Main Django app
├── templates/ # HTML templates (login, etc.)
├── db.sqlite3 # Default database (SQLite)
├── manage.py # Django management script
└── requirements.txt # Dependencies

## Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/saul0592/Inventory_supermarket_Django_APIs.git
   cd Inventory_supermarket_Django_APIs
Create a virtual environment

python3 -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows


**##Install dependencies**

pip install -r requirements.txt


**Apply migrations**

python manage.py migrate


**Run the development server**

python manage.py runserver


**Open in browser:**
👉 http://127.0.0.1:8000/

**🛠️ Tech Stack**

Python 3

Django

SQLite (default DB)

**Next Steps (to be implemented)**

User authentication (login & registration with Django forms)

CRUD APIs for product management

Admin dashboard

Unit testing and API documentation
