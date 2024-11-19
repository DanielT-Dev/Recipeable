from django.shortcuts import render, redirect
from .models import Recipe, Food
from recipes_app.utils.spoonacular import get_random_recipes
from .forms.FoodForm import FoodForm

def convert_all_foods_to_objects(foods):
    food_objects = []
    for food in foods:
        food_object = {
            "name": food.name,
            "image_url": food.image_url,
            "content": food.description,
        }
        food_objects.append(food_object)
    return food_objects

def add_recipe(request):
    if request.method == 'POST':
        form = FoodForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('home')  # Redirect to the homepage after saving
        else:
            # Re-render the form with errors
            return render(request, 'recipes_app/index.html', {'form': form})
    else:
        # If GET request, return the empty form
        form = FoodForm()
        return render(request, 'recipes_app/index.html', {'form': form})

def index(request):
    recipes = Recipe.objects.all()  # Fetch all recipes from the database
    foods = Food.objects.all()

    random_recipes = []  # get_random_recipes(number=3)  # Fetch random recipes

    # Handling form submission through add_recipe
    form = FoodForm()  # Initialize the form

    if request.method == 'POST':
        form = FoodForm(request.POST, request.FILES)  # Re-initialize form with POST data
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('home')  # Redirect to the homepage after saving

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
        'name': 'Pizza Margherita',
        'image_url': 'recipes_app/margherita_pizza.jpg',
        'content': "Pizza Margherita is a classic Italian pizza known for its simplicity and fresh ingredients...",
    }
    food2 = {
        'name': 'Caesar Salad',
        'image_url': 'recipes_app/caesar_salad.jpg',
        'content': "Caesar salad is a popular salad consisting of romaine lettuce, croutons, and Parmesan cheese...",
    }

    return render(request, 'recipes_app/index.html', {
        'recipes': recipes,
        'random_recipes': random_recipes,
        'foods': convert_all_foods_to_objects(foods),
        'saved_recipes_list': saved_recipes_list,
        'popular_recipes_list': popular_recipes_list,
        'new_recipes_list': new_recipes_list,
        'food1': food1,
        'food2': food2,
        'form': form,  # Pass the form to the template
    })
