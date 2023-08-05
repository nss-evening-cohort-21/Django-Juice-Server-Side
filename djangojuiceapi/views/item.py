"""View module for handling requests about Item"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from djangojuiceapi.models import Item

class ItemView(ViewSet):
    """DjangoJuice Item View"""
    
    