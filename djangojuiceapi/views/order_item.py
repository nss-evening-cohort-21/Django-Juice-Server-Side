"""View module for handling requests about song genres"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from djangojuiceapi.models import Order, Item, OrderItem


class OrderItemView(ViewSet):
    """DjangoJuice API order_item view"""
    
    def retrieve(self, request, pk):
      """Handle GET requests for a single order_item
      
      Returns:
          Response -- JSON serialized order_item
      """
      
      try:
          order_item = OrderItem.objects.get(pk=pk)
          
          serializer = OrderItemSerializer(order_item)
          return Response(serializer.data, status=status.HTTP_200_OK)
        
      except OrderItem.DoesNotExist as ex:
          return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
        
    def list(self, request):
      """Handle GET requests to get all order_items
    
      Returns:
          Response -- JSON serialized list of all order_items
      """
    
      order_items = OrderItem.objects.all()
      
      # filter to query order_items by order_id
      order_id = request.query_params.get('order_id', None)
      
      if order_id is not None:
        order_items = order_items.filter(order_id_id=order_id)
      
      serializer = OrderItemSerializer(order_items, many=True)
      return Response(serializer.data)
  
    def create(self, request):
        """Handle POST operations for order_item
        
        Returns
            Response -- JSON serialized order_item instance
        """
        
        order_id = Order.objects.get(pk=request.data["orderId"])
        item_id = Item.objects.get(pk=request.data["itemId"])
        
        order_item = OrderItem.objects.create(
            order_id=order_id,
            item_id=item_id,
            quantity=request.data["quantity"]
        )
        serializer = OrderItemSerializer(order_item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      
    def update(self, request, pk):
      """Handle PUT requests for an order_item
      
      Returns:
          Response -- Empty body with 204 status code
      """
      # get the order_item by the primary key
      order_item = OrderItem.objects.get(pk=pk)
      order_item.quantity = request.data["quantity"]
      
      # use the order_id as the foreign key to access order object
      order_id = Order.objects.get(pk=request.data["orderId"])
      order_item.order_id = order_id
      
      # use the item_id as the foreign key to access the item object
      item_id = Item.objects.get(pk=request.data["itemId"])
      order_item.item_id = item_id
      
      # save the updated order_item
      order_item.save()
      
      return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
      order_item = OrderItem.objects.get(pk=pk)
      order_item.delete()
      return Response(None, status=status.HTTP_204_NO_CONTENT)
      

class OrderItemSerializer(serializers.ModelSerializer):
  """JSON serializer for order_items"""

  class Meta:
      model = OrderItem
      fields = ('id', 'order_id', 'item_id', 'quantity')
      depth = 2
