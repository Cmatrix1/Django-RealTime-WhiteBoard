from django.shortcuts import render, get_object_or_404
from django.core.files.storage import default_storage

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from conference.models import ConferenceRoom
from board.models import ImageBoard
from datetime import datetime



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
    
