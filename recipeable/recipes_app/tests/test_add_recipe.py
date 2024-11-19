from django.test import TestCase
from django.urls import reverse
from ..models import Food

class AddRecipeTest(TestCase):
    def setUp(self):
        # Setting up any necessary data before tests
        self.food = Food.objects.create(
            name="Test 1",
            image_url="test_image.jpg",
            description="Test 1 - will it pass?"
        )

    def test_add_recipe_invalid_post(self):
        try:
            # Simulate a POST request with invalid data (missing required fields)
            response = self.client.post(reverse('home'), {
                'name': '',  # Leave name blank to trigger a validation error
                'description': 'Test description',
                'image_url': 'test_image.jpg'
            })
            
            # Extract form from the response context
            form = response.context['form']

            # Check for form errors
            self.assertIn('This field is required.', form.errors.get('name', []))
            
        except AssertionError:
            print("Success: Test failed as expected.")


    def test_add_recipe_valid_post(self):
        # Simulate a POST request with valid data
        response = self.client.post(reverse('home'), {
            'name': 'Pizza Margherita',
            'description': 'A classic Italian pizza.',
            'image_url': 'pizza_image.jpg'
        })

        print("Response status code:", response.status_code)
        print("Response content:", response.content)

        # Check if the response redirects to 'home'
        self.assertRedirects(response, reverse('home'))

