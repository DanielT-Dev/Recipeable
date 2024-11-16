from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='recipe_images/')
    instructions = models.TextField()

    def __str__(self):
        return self.name

class Food(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.CharField(max_length=255, default='recipes_app/default_image.jpg')  # Default value

    ingredients = models.TextField(blank=True, null=True)
    cuisine_types = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

