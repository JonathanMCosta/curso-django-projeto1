from django.test import TestCase
from django.urls import reverse


class RecipeURLsTest(TestCase):
    def test_recipe_the_url_is_correct(self):
        url = reverse('recipes:home')
        self.assertEqual(url, '/')
        
        
    def test_recipe_the_url_is_correct(self):
        url = reverse('recipes:category', args=[1])
        self.assertEqual(url, '/')
