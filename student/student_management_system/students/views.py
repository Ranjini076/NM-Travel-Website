from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Student, Report

# User Signup
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Student.objects.create(user=user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'students/register.html', {'form': form})

# User Login
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'students/login.html', {'error': 'Invalid credentials'})
    return render(request, 'students/login.html')

# User Logout
def logout_view(request):
    logout(request)
    return redirect('login')

# Dashboard
@login_required
def dashboard(request):
    student = Student.objects.get(user=request.user)
    reports = Report.objects.filter(student=student)
    return render(request, 'students/dashboard.html', {'student': student, 'reports': reports})

# Student Profile Page
@login_required
def student_profile(request):
    student = Student.objects.get(user=request.user)
    return render(request, 'students/student_profile.html', {'student': student})
