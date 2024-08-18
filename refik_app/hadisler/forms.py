from django import forms

from .models import Hadisler

class HadislerForm(forms.ModelForm):
    class Meta:
        model = Hadisler
        fields = ("tag", "title", "link")
        labels = {
            "tag": "Hafta Bilgisi ((Sene).(Dönem).(Hafta))",
            "title": "Hadis Başlığı:",
            "link": "Link"
        }