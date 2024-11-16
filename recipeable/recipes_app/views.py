from django.shortcuts import render
from .models import Recipe

def index(request):
    recipes = Recipe.objects.all()  # Fetch all recipes from the database
    return render(request, 'recipes_app/index.html', {'recipes': recipes})
