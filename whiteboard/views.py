from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views import View
from django.views.generic import TemplateView

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import ConferenceRoom, Message
from .serializers import MessageSerializer
from utils.permissions import IsUserInConfrence



class WhiteBoardView(TemplateView):
    template_name = "whiteboard/whiteboard.html"


class Conference(View):
    def dispatch(self, request, slug):
        self.room = get_object_or_404(ConferenceRoom, slug=slug)
        return super().dispatch(request, slug)
    
    def get(self, request: HttpRequest, slug: str):
        return render(request, "whiteboard/login_confrence.html", context={"room": self.room})
        
    def post(self, request: HttpRequest, slug: str):
        # Should Get User Here With Authenticate methods
        # And Create Member 
        return render(request, "whiteboard/confrence.html")
    


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
