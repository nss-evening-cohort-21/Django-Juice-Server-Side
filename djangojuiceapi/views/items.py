"""View module for handling requests about Product"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from djangojuiceapi.models import Item


class ItemView(ViewSet):
    """DjangoJuice Item View"""
    
    def retrieve(self, request, pk):
        """Handle GET Request for Single Item
        Returns:
            Response -- JSON Serialized Product
        """
        item = Item.objects.get(pk=pk)
        serializer = ItemSerializer(item)
        return Response(serializer.data)
      
    def list(self, request):

        item = Item.objects.all()
        serializer = ItemSerializer(item, many=True)
        return Response(serializer.data)

class ItemSerializer(serializers.ModelSerializer):
    """JSON Serializer For Item"""
    class Meta:
        model = Item
        fields = ('id', 'name', 'description', 'image_url', 'price')
        depth = 1
