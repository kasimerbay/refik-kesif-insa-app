from django.shortcuts import render

# Create your views here.
def portal(requests):
    return render(requests, "portal.html")