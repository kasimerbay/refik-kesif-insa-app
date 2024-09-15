from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpform
# Create your views here.

class LoginInterfaceView(LoginView):
    template_name = "home/login.html"

def index(requests):
    return render(requests, "home/home.html")

def generic(requests):
    return render(requests, "home/generic.html")

def logout_user(request):
    logout(request)
    messages.success(request, "You have succesfully logged out.")
    return redirect('login')

def register_user(request):
    if request.method == 'POST':
        form = SignUpform(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, "Successfully registered, Welcome!")
            return redirect('home')
    else:
        form = SignUpform
    
    return render(request, 'home/register.html', {'form':form})