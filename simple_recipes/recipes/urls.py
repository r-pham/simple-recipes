from django.urls import path

from simple_recipes.recipes import api_views


urlpatterns = [
    path('recipe', api_views.add_recipe),
    path('recipe/<recipe_id>', api_views.get_recipe),
    path('recipes', api_views.get_recipes)
]
