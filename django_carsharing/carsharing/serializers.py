from rest_framework import serializers
from .models import City, Car

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'
        
class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
