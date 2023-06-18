from rest_framework import serializers
from apps.foods.models import *

class FoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = food
        fields = ['food_name','serving_size', 'calories', 'carbon','protein','fat', 'cholesterol']




