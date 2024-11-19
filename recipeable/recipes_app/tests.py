from django.test import TestCase, Client
from django.urls import reverse
from .models import Recipe, Food
from .forms import FoodForm
from .views import convert_all_foods_to_objects
from unittest.mock import patch  # For mocking

class ConvertAllFoodsToObjectsTest(TestCase):
    def setUp(self):
        self.food = Food.objects.create(
            name="Test 1",
            image_url="test_image.jpg",
            description="Test 1 - will it pass?"
        )

    def test_convert_food_objects(self):
        foods = Food.objects.all()
        result = convert_all_foods_to_objects(foods)
        expected = [
            {
                "name": "Test 1",
                "image_url": "test_image.jpg",
                "content": "Test 1 - will it pass?"
            }
        ]
        self.assertEqual(result, expected)

    def test_empty_food_list(self):
        result = convert_all_foods_to_objects([])
        self.assertEqual(result, [])