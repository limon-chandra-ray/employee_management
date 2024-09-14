from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Login view
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Log the user in
            return redirect('employee-list')  # Redirect after successful login
        else:
            return render(request, 'users/login.html', {'error': 'Invalid credentials'})

    return render(request, 'users/login.html')

# Signup view
def signup_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Validate that passwords match
        if password != confirm_password:
            return render(request, 'users/signup.html', {'error': 'Passwords do not match'})

        # Check if the username is taken
        if User.objects.filter(username=username).exists():
            return render(request, 'users/signup.html', {'error': 'Username already taken'})

        # Create a new user
        user = User.objects.create_user(username=username, password=password)
        login(request, user)  # Log the user in after successful sign-up
        return redirect('employee-list')

    return render(request, 'users/signup.html')

# Logout view
def logout_view(request):
    logout(request)  # Log the user out
    return redirect('login')
