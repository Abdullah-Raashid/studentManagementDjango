# Student Management System (Django)

A role-based web application for managing student data, built with _Django 5_.

---

## Key Features

- Custom user model with email login and three roles: **Admin**, **Teacher**, **Student**
- Secure authentication: signup, login, logout, and password reset via email token.
- CRUD for students— create, list, view, update, delete
  - Stores parent/guardian information
  - Upload student profile images
- Extra-curricular **Clubs** (many-to-many) with automatic slug generation
- Real-time notifications via _Django Signals_
- **Asynchronous welcome e-mail** dispatched through _Celery_ & Redis
- CSV export of the complete student list streamed with Python _Generators_
- RESTful JSON API (`/api/students/`) built on **Django REST Framework**
- GraphQL endpoint (`/graphql`) powered by **Graphene-Django** (GraphiQL UI enabled)
- Management command `seed_students` to generate demo data
- Pytest test-suite & GitHub Actions CI pipeline
- Responsive templates & dashboard UI (Bootstrap 5, DataTables, ApexCharts, FullCalendar)

---

Follow the steps below on macOS/ Linux. On Windows, adapt the shell commands accordingly.

```bash
# Clone the repo
$ git clone git@github.com:Abdullah-Raashid/studentManagementDjango.git && cd student-management-django

# Create and activate a virtual environment
$ python3 -m venv venv
$ source venv/bin/activate  # windows: venv\Scripts\activate

# Install Python dependencies
$ pip install -r requirements.txt

# Apply database migrations
$ python manage.py migrate

# (Optional) create an admin user
$ python manage.py createsuperuser

# (Optional) seed the database with sample data
$ python manage.py seed_students --count 50

# (Optional) start Redis (required for Celery tasks)
$ docker run -p 6379:6379 -d redis:7-alpine

# (Optional) in a separate shell, start the Celery worker
$ celery -A Home worker --loglevel=info

# Run the development server
$ python manage.py runserver
```

Open http://127.0.0.1:8000 in your browser and log in with the credentials you created, or make an account using the sign-up menu and log in (recommended).

### Example GraphQL query

```graphql
{
  allStudents {
    id
    firstName
    lastName
    studentId
    studentClass
  }
}
```

---

## Project Layout (excerpt)

```
Home/            – Django project settings & Celery app
home_auth/       – Custom user model, auth views, decorators
school/          – Notification model & utilities
student/         – Core domain models, views, API, GraphQL schema, tests
static/          – CSS, JS, images
templates/       – HTML templates grouped by app
.github/         – GitHub Actions CI workflow
```
