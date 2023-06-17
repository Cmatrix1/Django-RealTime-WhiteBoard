from rest_framework import serializers
from .models import Message



class MessageSerializer(serializers.ModelSerializer):
    sender_name = serializers.SerializerMethodField()

    def get_sender_name(self, obj):
        sender = obj.sender
        return sender.name if sender else sender.user.username
    
    class Meta:
        model = Message
        fields = ['sender_name', 'content', 'created_at']
