"""View module for handling requests about Orders"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from djangojuiceapi.models import Order, User

class OrderView(ViewSet):
    """Djangojuice Order View"""
    
    def retrieve(self, request, pk):
        """Handle GET Request for Single Order
        Returns:
            Response -- JSON Serialized Order
        """
        order = Order.objects.get(pk=pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)
      
    def list(self, request):

        order = Order.objects.all()
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)
      
    def create(self, request):
        """Handle POST operations

        Returns
        Response -- JSON serialized Orders instance
        """
        user_id = User.objects.get(pk=request.data["userId"])
        
        orders = Order.objects.create(
            total=request.data["total"],
            timestamp=request.data["timestamp"],
            is_open=request.data["isOpen"],
            user_id=user_id,
        )
        serializer = OrderSerializer(orders)
        return Response(serializer.data)
      
    def update(self, request, pk):
        """Handle PUT requests for a order

        Returns:
        Response -- Empty body with 204 status code
        """

        order = Order.objects.get(pk=pk)
        order.timestamp = request.data["timestamp"]
        order.total = request.data["total"]
        order.is_open = request.data["isOpen"]
        # user_id = User.objects.get(pk=request.data["user_id"])
        # order.user_id = user_id
  
        order.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        """Delete order
        """
        order = Order.objects.get(pk=pk)
        order.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
   

class OrderSerializer(serializers.ModelSerializer):
    """JSON Serializer For Orders"""
    class Meta:
        model = Order
        fields = ('id', 'total', 'user_id', 'timestamp', 'is_open')
        depth = 1
