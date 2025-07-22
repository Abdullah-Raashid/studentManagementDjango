# Student Management System (Django)

A role-based web application for managing student data, built with Django 5.

## Features

- Custom user model with email login and three roles: **Admin**, **Teacher**, **Student**
- Secure authentication: signup, login, logout and password reset via email token (console backend in development)
- CRUD for students — create, list, view, update, delete
  - Stores parent/guardian information
  - Upload student profile images
- Extra-curricular **Clubs** (many-to-many) with automatic slug generation
- Notification system that records actions such as adding or deleting a student
- Management command `seed_students` to generate demo data
- Responsive templates & dashboard UI (Bootstrap 5, DataTables, ApexCharts, FullCalendar, etc.)

## Quickstart

Follow the steps below on macOS / Linux / WSL. On Windows, adapt the shell commands accordingly.

```bash
# 1. Clone the repo
$ git clone <your-fork-url> student-management-django && cd student-management-django

# 2. Create & activate a virtual environment (Python ≥ 3.10 recommended)
$ python3 -m venv venv
$ source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install Python dependencies
$ pip install --upgrade pip
$ pip install -r requirements.txt

# 4. Apply database migrations
$ python manage.py migrate

# 5. Create an admin user (optional but recommended)
$ python manage.py createsuperuser

# 6. (Optional) Seed the database with sample data
$ python manage.py seed_students --count 50

# 7. Run the development server
$ python manage.py runserver
```

Open http://127.0.0.1:8000 in your browser and log in with the credentials you created.

### Environment tweaks

- Email is sent to the console by default (`EMAIL_BACKEND = django.core.mail.backends.console.EmailBackend`).
- For production you will need to set real email credentials and `DEBUG = False`.
- Static files are served with **WhiteNoise**; run `python manage.py collectstatic` before deploying.

## Project layout (excerpt)

```
Home/            – Django project settings
home_auth/       – Custom user model & auth views
school/          – Notifications & utilities
student/         – Student/parent/club models & views
static/          – CSS, JS, images
templates/       – HTML templates grouped by app
```

## License

MIT — see `LICENSE` for details.
