from django.http import StreamingHttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

# TODO: Import serializers
# TODO: Import recipes service


def _get_recipes_service():
    pass


@api_view(['POST'])
def add_recipe(request: Request) -> Response:
    # TODO: Use a recipe serializer and validate it
    # TODO: Get recipes service and execute add_recipe
    return Response('add_recipe')


@api_view(['GET'])
def get_recipe(request: Request, recipe_id: int) -> Response:
    return Response('get_recipe')


@api_view(['GET'])
def get_recipes(request: Request) -> Response:
    return Response({'status': 'get_recipes'})
