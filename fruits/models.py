from django.db import models
from uuid import uuid4

from regions.models import Regions

# Create your models here.

class Fruits (models.Model):
    id_fruit = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name_fruit = models.CharField(max_length=100)
    region = models.ForeignKey(Regions, on_delete=models.CASCADE)
    
