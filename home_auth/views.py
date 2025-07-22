from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser, PasswordResetRequest
from django.utils import timezone
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.utils.crypto import get_random_string


def signup_view(request):
    if request.method == 'POST':
        # ---------------------------
        # 1. Extract form data
        # ---------------------------
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        email = request.POST.get('email', '').strip().lower()
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        role = request.POST.get('role')  # student | teacher | admin

        # ---------------------------
        # 2. Basic validation
        # ---------------------------
        if not role:
            messages.error(request, 'Please select a role.')
            return redirect('signup')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect('signup')

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'A user with that email already exists.')
            return redirect('signup')

        # ---------------------------
        # 3. Create user and assign role
        # ---------------------------
        user = CustomUser.objects.create_user(
            username=email,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )

        if role == 'student':
            user.is_student = True
        elif role == 'teacher':
            user.is_teacher = True
        elif role == 'admin':
            user.is_admin = True
        else:
            # Should never happen because of earlier check, but guard anyway
            messages.error(request, 'Invalid role selected.')
            user.delete()
            return redirect('signup')

        user.save()

        # ---------------------------
        # 4. Log user in & redirect
        # ---------------------------
        login(request, user)
        messages.success(request, 'Signup successful!')
        return redirect('index')

    return render(request, 'authentication/register.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip().lower()
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)
        if user is None:
            messages.error(request, 'Invalid credentials')
            return redirect('login')

        # Determine redirect target based on role
        if user.is_admin:
            redirect_url = 'admin_dashboard'
        elif user.is_teacher:
            redirect_url = 'teacher_dashboard'
        elif user.is_student:
            redirect_url = 'dashboard'
        else:
            messages.error(request, 'Invalid user role')
            return redirect('index')

        # Successful authentication & valid role – log in and redirect
        login(request, user)
        messages.success(request, 'Login successful!')
        return redirect(redirect_url)

    return render(request, 'authentication/login.html')


def forgot_password_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        user = CustomUser.objects.filter(email=email).first()
        
        if user:
            token = get_random_string(32)
            reset_request = PasswordResetRequest.objects.create(user=user, email=email, token=token)
            reset_request.send_reset_email()
            messages.success(request, 'Reset link sent to your email.')
        else:
            messages.error(request, 'Email not found.')
    
    return render(request, 'authentication/forgot-password.html')  # Render forgot password template


def reset_password_view(request, token):
    reset_request = PasswordResetRequest.objects.filter(token=token).first()
    
    if not reset_request or not reset_request.is_valid():
        messages.error(request, 'Invalid or expired reset link')
        return redirect('index')

    if request.method == 'POST':
        new_password = request.POST['new_password']
        reset_request.user.set_password(new_password)
        reset_request.user.save()
        messages.success(request, 'Password reset successful')
        return redirect('login')

    return render(request, 'authentication/reset_password.html', {'token': token})  # Render reset password template


def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('index')
