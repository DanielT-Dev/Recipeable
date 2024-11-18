from django.shortcuts import render, redirect
from .models import Recipe
from .models import Food
from recipes_app.utils.spoonacular import get_random_recipes

from .forms.FoodForm import FoodForm

def index(request):
    recipes = Recipe.objects.all()  # Fetch all recipes from the database
    foods =     Food.objects.all()

    random_recipes = [] #get_random_recipes(number=3)  # Fetch 3 random recipes

    # Handling form submission
    if request.method == 'POST':
        form = FoodForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()  # Save the food data
            return redirect('home')  # Redirect to home after saving

    else:
        form = FoodForm()  # Initialize an empty form for GET requests

    saved_recipes_list = {
        'name': "Saved",
        'image_url': "recipes_app/save1.png",
        'content': [],
    }
    popular_recipes_list = {
        'name': "Popular",
        'image_url': "recipes_app/like1.png",
        'content': [],
    }
    new_recipes_list = {
        'name': "New",
        'image_url': "recipes_app/fire1.png",
        'content': [],
    }

    food1 = {
        'name': 'Pizza Mergherita',
        'image_url': 'recipes_app/margherita_pizza.jpg',
        'content': "Pizza Margherita is a classic Italian pizza known for its simplicity and fresh ingredients. It features a thin crust topped with tomato sauce, fresh mozzarella, and basil leaves, representing the colors of the Italian flag. Drizzled with olive oil, it's a perfect balance of flavors: tangy tomatoes, creamy cheese, and aromatic basil.",
    }
    food2 = {
        'name': 'Caesar Salad',
        'image_url': 'recipes_app/caesar_salad.jpg',
        'content': "Caesar salad is a popular salad consisting of romaine lettuce, croutons, and Parmesan cheese, all tossed in a creamy dressing made from garlic, anchovies, egg yolks, lemon juice, Dijon mustard, and olive oil. Often, it is topped with black pepper and sometimes additional ingredients like grilled chicken or bacon.",
    }

    form = FoodForm()

    return render(request, 'recipes_app/index.html', {
        'recipes': recipes,
        'random_recipes': random_recipes,
        'foods': foods,
        'saved_recipes_list': saved_recipes_list,
        'popular_recipes_list': popular_recipes_list,
        'new_recipes_list': new_recipes_list,
        'food1': food1,
        'food2': food2,
    })
