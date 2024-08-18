from django.urls import path
from . import views


urlpatterns = [
    path("", views.HadislerListView.as_view(), name="hadis.list"),
    path("hadis/<int:pk>/", views.HadisDetailView.as_view(), name="hadis.detail"),
    path("add/", views.HadislerCreateView.as_view(), name="hadis.add"),
    path("hadis/<int:pk>/delete", views.HadislerDeleteView.as_view(), name="hadis.delete"),
    path("hadis/<int:pk>/update", views.HadislerUpdateView.as_view(), name="hadis.update"),
]
