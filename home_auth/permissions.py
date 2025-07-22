from functools import wraps
from django.core.exceptions import PermissionDenied


def _check_role(user, *, student=False, teacher=False, admin=False):
    """Return True if the user has at least one of the allowed roles."""
    if not user.is_authenticated:
        return False

    if admin and getattr(user, "is_admin", False):
        return True  # admin always allowed when admin flag present

    if student and getattr(user, "is_student", False):
        return True

    if teacher and getattr(user, "is_teacher", False):
        return True

    # Allow admin to act as teacher or student by default
    if getattr(user, "is_admin", False):
        return True

    return False


def role_required(*, student=False, teacher=False, admin=False):
    """Decorator factory for restricting access to users with given role flags.

    Usage::
        @role_required(admin=True)
        def view(request): ...
    """

    def decorator(view_func):
        @wraps(view_func)
        def _wrapped(request, *args, **kwargs):
            if _check_role(request.user, student=student, teacher=teacher, admin=admin):
                return view_func(request, *args, **kwargs)
            raise PermissionDenied

        return _wrapped

    return decorator


# Concrete shortcuts
student_required = role_required(student=True)
teacher_required = role_required(teacher=True)
admin_required = role_required(admin=True) 