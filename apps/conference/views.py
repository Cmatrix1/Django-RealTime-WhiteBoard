from datetime import datetime

from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.core.files.storage import default_storage
from django.views.generic import TemplateView
from django.views import View

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import ConferenceRoom


# class Conference(View):
#     def dispatch(self, request, slug):
#         self.room = get_object_or_404(ConferenceRoom, slug=slug)
#         return super().dispatch(request, slug)
    
#     def get(self, request: HttpRequest, slug: str):
#         return render(request, "whiteboard/login_conference.html", context={"room": self.room})
        
#     def post(self, request: HttpRequest, slug: str):
#         # Should Get User Here With Authenticate methods
#         # And Create Member 
#         return render(request, "whiteboard/conference.html")
    

class Conference(View):
    def dispatch(self, request, slug):
        self.room = get_object_or_404(ConferenceRoom, slug=slug)
        return super().dispatch(request, slug)
    
    def get(self, request: HttpRequest, slug: str):
        return render(request, "conference/conference.html", context={"room": self.room})