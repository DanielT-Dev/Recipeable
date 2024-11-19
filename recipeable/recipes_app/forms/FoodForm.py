from django import forms
from ..models import Food

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'description', 'image_url', 'ingredients', 'cuisine_types', 'price']

    description = forms.CharField(widget=forms.Textarea, required=True)
    ingredients = forms.CharField(widget=forms.Textarea, required=False)  # Change to False to allow empty
    cuisine_types = forms.CharField(widget=forms.Textarea, required=False)  # Change to False to allow empty
    price = forms.DecimalField(required=False)  # Allow price to be optional, too
