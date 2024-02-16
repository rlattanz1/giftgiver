from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Gift
from .serializers import GiftSerializer


# Create your views here.

@api_view(['GET'])

def getRoutes(request):
    routes = [
        {
            'Endpoint': '/gifts/',
            'method': 'GET',
            'body': None,
            'url': None,
            'price': None,
            'description': 'Returns an array of gifts and url links'
        },
        {
            'Endpoint': '/gifts/id/',
            'method': 'GET',
            'body': None,
            'url': None,
            'price': None,
            'description': 'Returns a single gift and a url link'
        },
        {
            'Endpoint': '/gifts/create/',
            'method': 'POST',
            'body': {'body': ""},
            'url': {'url': ""},
            'price': {'price': ""},
            'description': 'Creates a new gift with data sent in a post request'
        },
        {
            'Endpoint': '/gifts/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'url': {'url': ""},
            'price': {'price': ""},
            'description': 'Updates a specific gift with data sent in a post request'
        },
        {
            'Endpoint': '/gifts/id/delete/',
            'method': 'DELETE',
            'body': None,
            'url': None,
            'price': None,
            'description': 'Deletes an existing gift'
        }
    ]
    return Response(routes)

@api_view(['GET'])
def getGifts(request):
    gifts = Gift.objects.all()
    serializer = GiftSerializer(gifts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getGift(request, pk):
    gift = Gift.objects.get(id=pk)
    serializer = GiftSerializer(gift, many=False)
    return Response(serializer.data)
