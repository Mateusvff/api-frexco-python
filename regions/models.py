from uuid import uuid4
from django.db import models
from django.forms import CharField
from uuid import uuid4

# Create your models here.

class Regions(models.Model):
    id_region = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name_region = models.CharField(max_length=50)
