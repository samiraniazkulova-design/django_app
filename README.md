# Django Web Application

A robust web application built using the Django framework, featuring a structured backend, SQLite database integration, and local development configuration.

## Features
* **Django Framework**: Built with modular app architecture and Python's powerful ORM.
* **Database**: Configured with SQLite for seamless local development and data management.
* **Version Control**: Managed and tracked using Git and GitHub.

## Project Structure
```text
django_app/
│
├── db.sqlite3       # SQLite database file
├── manage.py        # Django's command-line utility for administrative tasks
└── README.md        # Project documentation

git clone [https://github.com/samiraniazkulova-design/django_app.git](https://github.com/samiraniazkulova-design/django_app.git)
cd django_app

python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

pip install django

python manage.py makemigrations
python manage.py migrate

python manage.py runserver
