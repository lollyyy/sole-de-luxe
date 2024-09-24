from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.

class ShoesEntry(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    color = models.CharField(max_length=100)
    condition = models.CharField(max_length=100)
    release_year = models.IntegerField()

    @property
    def is_vintage(self):
        return self.release_year < 2010