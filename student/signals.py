from django.db.models.signals import post_save
from django.dispatch import receiver
from student.models import Student
from school.models import Notification


@receiver(post_save, sender=Student)
def create_student_notification(sender, instance, created, **kwargs):
    if created:
        msg = f"Added student: {instance.first_name} {instance.last_name}"
    else:
        msg = f"Updated student: {instance.first_name} {instance.last_name}"

    # attach to whoever performed action if available (skip if called from shell)
    user = getattr(instance, "_actor", None)
    if user:
        Notification.objects.create(user=user, message=msg) 