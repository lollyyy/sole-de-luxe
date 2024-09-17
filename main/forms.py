from django.forms import ModelForm
from main.models import ShoesEntry

class ShoesEntryForm(ModelForm):
    class Meta:
        model = ShoesEntry
         # code dibawah ini diganti sesuai dari isi models.py
        fields = ["name", "price", "description", "color", "condition", "release_year"]