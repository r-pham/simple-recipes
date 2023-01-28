from rest_framework import serializers

from simple_recipes.models import Recipe


class RecipeSerializer(serializers.Serializer):
    name = serializers.CharField()
    ingredients = serializers.JSONField()
    instructions = serializers.CharField()
