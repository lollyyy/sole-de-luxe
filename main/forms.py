from django.forms import ModelForm
from main.models import ShoesEntry
from django.utils.html import strip_tags

class ShoesEntryForm(ModelForm):
    class Meta:
        model = ShoesEntry
         # code dibawah ini diganti sesuai dari isi models.py
        fields = ["name", "price", "description", "color", "condition", "release_year"]

        def clean_name(self):
            name = self.cleaned_data["name"]
            return strip_tags(name)

        def clean_description(self):
            description = self.cleaned_data["description"]
            return strip_tags(description)
        
        def clean_color(self):
            color = self.cleaned_data["color"]
            return strip_tags(color)

        def clean_condition(self):
            condition = self.cleaned_data["condition"]
            return strip_tags(condition)