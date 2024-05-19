from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def program(requests):
    return HttpResponse("<h1>Refik Keşif İnşa Programına Hoş Geldiniz...</h1>")