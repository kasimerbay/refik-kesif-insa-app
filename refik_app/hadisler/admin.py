from django.contrib import admin

from . import models

# Register your models here.
class HadislerAdmin(admin.ModelAdmin):
    list_display = ("tag","title", )
    sortable_by = ("tag", "title")

admin.site.register(models.Hadisler, HadislerAdmin)