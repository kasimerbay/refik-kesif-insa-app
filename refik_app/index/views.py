from django.shortcuts import render, redirect

# Create your views here.
def index(requests):
    return render(requests, "index.html")