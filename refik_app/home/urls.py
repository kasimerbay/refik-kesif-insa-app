from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="home"),
    path('generic/', views.generic, name="generic"),
    path('login/', views.LoginInterfaceView.as_view(), name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_user, name="register"),
]
