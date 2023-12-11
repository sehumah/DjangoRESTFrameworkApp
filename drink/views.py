from django.shortcuts import render
from drink.models import Drink
from django.http import JsonResponse
from drink.serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# holds all the endpoints: URLs to access data from


@api_view(['GET', 'POST'])
def drinks(request):
    # get all the drinks, serialize them & return them in json
    if request.method == 'GET':
        drinks = Drink.objects.all()
        drink_serializer = DrinkSerializer(drinks, many=True)
        return JsonResponse({'drinks': drink_serializer.data})

    # add a drink to the database: take the data sent, deserialize it and create a drink object out of it
    if request.method == 'POST':
        drink_serializer = DrinkSerializer(data=request.data)
        if drink_serializer.is_valid():
            drink_serializer.save()
            return Response(drink_serializer.data, status=status.HTTP_201_CREATED)
