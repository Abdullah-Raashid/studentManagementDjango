from django.http import HttpResponse, JsonResponse, HttpResponseForbidden
from django.shortcuts import render
from .models import Notification
from home_auth.permissions import admin_required, teacher_required, student_required

# Create your views here.

def index(request):
    return render(request, "authentication/login.html")

@student_required
def dashboard(request):
    unread_notification = Notification.objects.filter(user=request.user, is_read=False)
    unread_notification_count = unread_notification.count()
    return render(request, "students/student-dashboard.html")



def mark_notification_as_read(request):
    if request.method == 'POST':
        notification = Notification.objects.filter(user=request.user, is_read=False)
        notification.update(is_read=True)
        return JsonResponse({'status': 'success'})
    return HttpResponseForbidden()

def clear_all_notification(request):
    if request.method == "POST":
        notification = Notification.objects.filter(user=request.user)
        notification.delete()
        return JsonResponse({'status': 'success'})
    return HttpResponseForbidden()

@admin_required
def admin_dashboard(request):
    """Render the admin dashboard (currently using Home/index.html template)."""
    return render(request, "Home/index.html")


@teacher_required
def teacher_dashboard(request):
    """Render the teacher dashboard. Placeholder: reuse student dashboard template until a specific one is created."""
    return render(request, "students/student-dashboard.html")


def edit_student_static(request):
    """Serve the generic edit-student page (static version)."""
    return render(request, "students/edit-student.html")

def blank_page(request):
    """Simple placeholder blank page used for sidebar demo link."""
    return render(request, "Home/blank-page.html")