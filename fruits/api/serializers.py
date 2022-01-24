from rest_framework import serializers
from fruits import models


class FruitSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Fruits
        fields = '__all__'
        