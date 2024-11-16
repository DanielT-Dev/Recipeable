from django.shortcuts import render
from .models import Recipe
from .models import Food

def index(request):
    recipes = Recipe.objects.all()  # Fetch all recipes from the database
    foods = Food.objects.all()

    return render(request, 'recipes_app/index.html', {
        'recipes': recipes,
        'foods': foods,
    })

def food_card_view(request):
    # Retrieve food items (you can use all, filter, etc.)
    foods = Food.objects.all()  # Or filter specific foods
    
    # Pass the data to the template
    return render(request, 'recipes_app/food_card.html', {'foods': foods})
