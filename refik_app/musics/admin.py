from django.contrib import admin

# Register your models here.
from . import models

class MusicsAdmin(admin.ModelAdmin):
    list_display = ("id","title", "composer")
    sortable_by = "id"

admin.site.register(models.Musics, MusicsAdmin)