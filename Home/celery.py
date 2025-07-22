from __future__ import absolute_import, unicode_literals
import os

from celery import Celery

# Set default Django settings module for 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Home.settings")

app = Celery("student_management")

# Using a string here means the worker does not have to serialize
# the configuration object to child processes.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    """A no-op task to test the worker."""
    print(f"Request: {self.request!r}") 