from rest_framework import serializers
from .models import Food

class FoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Food
        fields = ('food_name', 'weight', 'fiber', 'vitamin_a', 'vitamin_b6', 'vitamin_b9', 'vitamin_b12', 'vitamin_c',
                  'vitamin_d', 'vitamin_e', 'calcium', 'omega_3', 'entryID')
