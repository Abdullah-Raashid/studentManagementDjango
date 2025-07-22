# Student Management System (Django)

A role-based web application for managing student data, built with *Django 5*.

## Features

- Custom user model with email login and three roles: **Admin**, **Teacher**, **Student**
- Secure authentication: signup, login, logout, and password reset via email token.
- CRUD for students— create, list, view, update, delete
  - Stores parent/guardian information
  - Upload student profile images
- Extra-curricular **Clubs** (many-to-many) with automatic slug generation
- A notification system that records actions such as adding or deleting a student
- Management command `seed_students` to generate demo data
- Responsive templates & dashboard UI (Bootstrap 5, DataTables, ApexCharts, and FullCalendar)

## Quickstart

Follow the steps below on macOS/ Linux. On Windows, adapt the shell commands accordingly.

```bash
# Clone the repo
$ git clone git@github.com:Abdullah-Raashid/studentManagementDjango.git && cd student-management-django

# Create and activate a virtual environment
$ python3 -m venv venv
$ source venv/bin/activate  # Windows: venv\Scripts\activate

# Install Python dependencies
$ pip install --upgrade pip
$ pip install -r requirements.txt

# Apply database migrations
$ python manage.py migrate

# Create an admin user (optional)
$ python manage.py createsuperuser

# Seed the database with sample data 
$ python manage.py seed_students --count 50

# Run the development server
$ python manage.py runserver
```

Open http://127.0.0.1:8000 in your browser and log in with the credentials you created, or make an account using the sign-up menu and log in (recommended).

## Project layout (excerpt)

```
Home/            – Django project settings
home_auth/       – Custom user model & auth views
school/          – Notifications & utilities
student/         – Student/parent/club models & views
static/          – CSS, JS, images
templates/       – HTML templates grouped by app
```
