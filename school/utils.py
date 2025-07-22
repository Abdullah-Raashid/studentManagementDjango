from school.models import Notification


def create_notification(user, message):
    """Create a notification attached to a user."""
    if user and message:
        Notification.objects.create(user=user, message=message) 