from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_welcome_email(email: str, first_name: str) -> str:
    """Send welcome email asynchronously."""
    send_mail(
        subject="Welcome to Django School",
        message=f"Hi {first_name},\n\nThank you for registering to our school.",
        from_email="no-reply@school.local",
        recipient_list=[email],
        fail_silently=False,
    )
    return "Email sent" 