from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Hadisler(models.Model):
    tag = models.CharField(max_length=10)
    title = models.CharField(max_length=200)
    link = models.URLField(max_length=300)
    added = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, verbose_name="İdareci", on_delete=models.CASCADE, related_name="hadisler")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("hadis.detail", kwargs={"pk": self.pk})

    def edit(self):
        return reverse("hadis.update", kwargs={"pk": self.pk})

    def remove(self):
        return reverse("hadis.delete", kwargs={"pk": self.pk})

    def add(self):
        return reverse("hadis.add")

    def list(self):
        return reverse("hadis.list")
