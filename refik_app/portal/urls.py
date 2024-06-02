from django.urls import path
from.views import portal

urlpatterns = [
    path('', portal, name="portal")
]
