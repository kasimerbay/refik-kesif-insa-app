from django.urls import path
from . import views


urlpatterns = [
    path("", views.MusicListView.as_view(), name="music.list"),
    path("music/<int:pk>", views.MusicDetailView.as_view(), name="music.detail"),
    path("musics/add", views.MusicCreateView.as_view(), name="music.add"),
    path("music/<int:pk>/delete", views.MusicDeleteView.as_view(), name="music.delete"),
    path("music/<int:pk>/update", views.MusicUpdateView.as_view(), name="music.update"),
]
