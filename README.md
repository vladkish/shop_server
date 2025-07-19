# 🛍️ Shop Server

An online store built with Django, featuring user registration, authentication, shopping cart, and product category filtering.

## 🚀 Features

- User registration and login  
- Logout functionality  
- Shopping cart: add, decrease quantity, remove, and clear  
- Product filtering by category  
- User profile: edit info, delete account  
- Error handling and improved UI (e.g. glowing basket button)

## 🗂 Project Structure

- `manage.py` — Django’s main command-line utility  
- `db.sqlite3` — project database  
- `requirements.txt` — Python dependencies  
- `media/` — uploaded product images  
- `static/` — CSS, JS, and static files  
- `products/` — app for products and category filters  
- `users/` — app for authentication and user profile  
- `store/` — project configuration and routing  
- `venv/` — virtual environment (not tracked by Git)

## ⚙️ Installation & Running

1. Clone the repository:  
   `git clone https://github.com/vladkish/shop_server.git`  
   `cd shop_server`

2. Create and activate a virtual environment:   
   `source venv/bin/activate` (Mac/Linux)  
   `venv\Scripts\activate` (Windows)

3. Install dependencies:  
   `pip install -r requirements.txt`

4. Apply migrations:  
   `cd server`
   `python manage.py migrate`

5. (Optional) Create a superuser:  
   `python manage.py createsuperuser`

6. Run the development server:  
   `python manage.py runserver`

7. Open in browser:  
   [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## 📌 Useful Routes

- `/admin/` — Django admin panel  
- `/login/` and `/register/` — login and registration pages  
- `/profile/` — user profile page  
- `/` — homepage with products and category filtering

## 🧑‍💻 Author

[@vladkish](https://github.com/vladkish)
