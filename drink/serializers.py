from rest_framework import serializers
from drink.models import Drink

# serializers describes the process of going from a python object to JSON


class DrinkSerializer(serializers.ModelSerializer):
    class Meta:  # metadata describing the model
        model = Drink
        fields = ['id', 'name', 'description', 'created_at', 'updated_at']