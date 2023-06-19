from rest_framework import serializers
from .models import Message



class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.SerializerMethodField()

    def get_sender(self, obj):
        sender = obj.sender
        return sender.name if sender else sender.user.username
    
    class Meta:
        model = Message
        fields = ['sender', 'content', 'created_at']
