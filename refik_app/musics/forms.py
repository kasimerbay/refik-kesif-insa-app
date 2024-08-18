from django import forms

from .models import Musics

class MusicForm(forms.ModelForm):
    class Meta:
        model = Musics
        fields = ("title", "composer", "link", "is_east")
        labels = {
            "title": "Parçanın Adı:",
            "composer": "Bestekar",
            "link": "Link:",
            "is_east":"Doğu Medeniyeti",
        }