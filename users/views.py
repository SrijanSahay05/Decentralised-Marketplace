from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import make_password
from .models import CustomUser, UserProfile

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = make_password(request.POST['password1'])
        wallet_address = request.POST['wallet_address']
        print(f"Username: {username}, Email: {email}, Password: {password}, Wallet Address: {wallet_address}")
        try:
            user = CustomUser.objects.create(username=username, email=email, password=password)
            user.save()
            print(f"User created: {user}")
        except Exception as e:
            print(f"Error: {e}")
        try:
            user = CustomUser.objects.get(username=username)
            profile = UserProfile.objects.create(user=user, wallet_address=wallet_address)
            profile.save()
            print(f"Profile created: {profile}")
        except Exception as e:
            print(f"Error: {e}")
        login(request, user)
        return redirect('index')
    
    return render(request, 'users/signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(f"Username: {username}, Password: {password}")
        try:
            user = CustomUser.objects.get(username=username)
            if user.check_password(password):
                login(request, user)
                return redirect('index')
        except Exception as e:
            print(f"Error: {e}")
    return render(request, 'users/login.html')

def logout_view(request):
    logout(request)
    return redirect('index')