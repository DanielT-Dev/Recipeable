from django import forms
from ..models import Food  # Ensure the correct import path

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'description', 'price', 'image_url', 'ingredients', 'cuisine_types']

    description = forms.CharField(widget=forms.Textarea, required=True)
    ingredients = forms.CharField(widget=forms.Textarea, required=True)
    price = forms.DecimalField(min_value=0, required=True)

