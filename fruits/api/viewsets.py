from statistics import mode
from rest_framework.viewsets import ModelViewSet
from fruits import models
from rest_framework import viewsets
from fruits.api import serializers


class FruitViewSet(viewsets.ModelViewSet):
    queryset = models.Fruits.objects.all()
    serializer_class = serializers.FruitSerializer