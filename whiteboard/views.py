from datetime import datetime

from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.core.files.storage import default_storage
from django.views.generic import TemplateView
from django.views import View

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import ConferenceRoom, Message, ImageBoard
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



class SaveImageAPIView(APIView):
    def post(self, request, slug):
        file = request.FILES.get('image')
        if not file:
            return Response({'success': False, 'message': 'No image file provided.'}, status=status.HTTP_400_BAD_REQUEST)

        room = get_object_or_404(ConferenceRoom, slug=slug).name
        time_str = datetime.now().strftime('%Y%m%d-%H%M%S')
        filename = f'{room}-{time_str}.png'
        file_path = default_storage.save(f"media/board/{filename}", file)
        image_board = ImageBoard(room=room, image=file_path)
        image_board.save()
        return Response({'success': True, 'file_path': file_path})