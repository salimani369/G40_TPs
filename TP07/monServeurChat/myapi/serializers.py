from rest_framework import serializers
from .models import Message

class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        # Les champs exposés par l'API en JSON
        fields = ('source', 'to', 'body')

