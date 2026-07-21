# 🌐 Mini Social Network (Django Monolith)

A lightweight social network application built entirely as a **Django monolith**. It features core social features including user profiles, posts feed, and interactive comments, demonstrating clean MVC architecture and database management.

---

## 🚀 Features

* **User Profiles:** Registration, authentication, and customizable user profiles.
* **Posts Feed:** Create, read, and delete posts to share updates in real-time.
* **Interactive Comments:** Leave comments on posts to foster community engagement.
* **Django Admin:** Built-in administrative dashboard for managing users, posts, and comments effortlessly.

---

## 🛠️ Tech Stack

* **Framework:** Django (MVT / Monolith architecture)
* **Database:** PostgreSQL / SQLite
* **Frontend:** Django Templates, HTML/CSS
* **Tools:** Postman (for testing database or API endpoints if extended)

---

## ⚙️ Installation & Setup

Follow these steps to run the project locally on your machine:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/tim41ek/your-repo-name.git](https://github.com/tim41ek/your-repo-name.git)
   cd your-repo-name
Create and activate a virtual environment:

python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
Install dependencies:

pip install -r requirements.txt
Apply database migrations:

python manage.py makemigrations
python manage.py migrate
Create a superuser (to manage posts and users via Admin panel):

python manage.py createsuperuser
Run the development server:

python manage.py runserver
Open your browser and navigate to http://127.0.0.1:8000/
