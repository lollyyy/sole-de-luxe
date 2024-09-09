from django.db import models

# Create your models here.
from django.db import models

class MoodEntry(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    color = models.CharField(max_length=100)
    condition = models.CharField(max_length=100)
    release_year = models.IntegerField()

    @property
    def is_vintage(self):
        return self.release_year < 2010