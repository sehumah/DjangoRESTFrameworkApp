from django.shortcuts import render
from drink.models import Drink
from django.http import JsonResponse
from drink.serializers import DrinkSerializer

# holds all the endpoints: URLs to access data from


def drinks(request):
    # get all the drinks, serialize them & return them in json
    drinks = Drink.objects.all()
    drink_serializer = DrinkSerializer(drinks, many=True)
    return JsonResponse(drink_serializer.data, safe=False)
