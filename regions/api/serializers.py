from rest_framework import serializers
from regions import models

class RegionSerializer(serializers.ModelSerializer):
    class Meta: 
        model = models.Regions
        fields = '__all__'