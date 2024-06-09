from django.shortcuts import render, redirect

# Create your views here.
def index(requests):
    return render(requests, "index.html")

def generic(requests):
    return render(requests, "generic.html")