from django.shortcuts import render

from rest_framework import viewsets
from .serializers import MessageSerializer
from .models import Message

class MessageViewSet(viewsets.ModelViewSet):
    # Récupère tous les messages triés par expéditeur
    queryset = Message.objects.all().order_by('source')
    # Utilise notre sérialiseur pour convertir en JSON
    serializer_class = MessageSerializer