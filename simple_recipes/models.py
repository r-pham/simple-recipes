from django.db import models


class Recipe(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    ingredients = models.JSONField(null=False)
    instructions = models.TextField(null=False)

