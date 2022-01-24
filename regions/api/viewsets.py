from pyexpat import model
from rest_framework import viewsets
from regions.api import serializers
from regions import models


class RegionViewSet(viewsets.ModelViewSet):
    queryset = models.Regions.objects.all()
    serializer_class = serializers.RegionSerializer