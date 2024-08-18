from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
# Create your views here.

class LogoutInterfaceView(LogoutView):
    template_name = "home/logout.html"
    next_page = "/"

class LoginInterfaceView(LoginView):
    template_name = "home/login.html"

def index(requests):
    return render(requests, "home/home.html")

def generic(requests):
    return render(requests, "home/generic.html")
