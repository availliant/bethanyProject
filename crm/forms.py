from django import forms
from .models import Food, Entry


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ('entryID',)

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ('food_name', 'weight', 'fiber', 'vitamin_a', 'vitamin_b6', 'vitamin_b9', 'vitamin_b12', 'vitamin_c',
                  'vitamin_d', 'vitamin_e', 'calcium', 'omega_3', 'entryID')

