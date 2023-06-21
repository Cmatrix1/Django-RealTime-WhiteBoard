from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from conference.models import ConferenceRoom
from message.models import Message
from message.serializers import MessageSerializer


class ConferenceRoomMessagesAPI(APIView):
    model = Message
    serializer_class = MessageSerializer
    
    def get(self, request, slug):
        room = get_object_or_404(ConferenceRoom, slug=slug)
        if room.is_participant(request.user):
            messages = room.messages.all()
            serializer = self.serializer_class(messages, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)