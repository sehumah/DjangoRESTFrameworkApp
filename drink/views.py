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
        # return JsonResponse({'drinks': drink_serializer.data})
        return Response(data=drink_serializer.data)  # use this new Response behavior instead

    # add a drink to the database: take the data sent, deserialize it and create a drink object out of it
    if request.method == 'POST':
        drink_serializer = DrinkSerializer(data=request.data)
        if drink_serializer.is_valid():
            drink_serializer.save()
            return Response(drink_serializer.data, status=status.HTTP_201_CREATED)

# the Response() isn't JSON specific which allows us to see an HTML view of the page where
# we can work with the data through the web page, similar to the admin panel


@api_view(['GET', 'PUT', 'DELETE'])
def detail(request, drink_id):
    # get the drink from the DB using its id. check to see if the given id is valid
    try:
        drink = Drink.objects.get(pk=drink_id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        drink_serializer = DrinkSerializer(drink)
        return Response(data=drink_serializer.data)

    elif request.method == 'PUT':
        drink_serializer = DrinkSerializer(drink, data=request.data)
        if drink_serializer.is_valid():
            drink_serializer.save()
            return Response(drink_serializer.data)  # give that data back
        else:
            return Response(drink_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
