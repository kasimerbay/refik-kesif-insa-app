from django.db import models
from django.urls import reverse
# Create your models here.

class Musics(models.Model):
    title = models.CharField(max_length=50)
    composer = models.CharField(max_length=40)
    link = models.URLField(max_length=300)
    is_east = models.BooleanField()
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("music.detail", kwargs={"pk": self.pk})

    def edit(self):
        return reverse("music.update", kwargs={"pk": self.pk})

    def remove(self):
        return reverse("music.delete", kwargs={"pk": self.pk})
    
    def add(self):
        return reverse("music.add")
    
    def list(self):
        return reverse("music.list")