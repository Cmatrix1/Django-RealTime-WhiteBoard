from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.views import View

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from conference.models import ConferenceRoom, Participant
from conference.forms import GuestLoginForm, UserLoginForm


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
    

class Conference(View):
    template_name = 'conference/login_conference.html'
    conference_template_name = 'conference/conference.html'

    def dispatch(self, request, slug):
        self.room = get_object_or_404(ConferenceRoom, slug=slug)
        request.session['room_slug'] = slug
        return super().dispatch(request, slug)
    
    def get(self, request, slug):
        guest_form = GuestLoginForm()
        user_form = UserLoginForm()
        return render(request, self.template_name, {'guest_form': guest_form, 'user_form': user_form, 'room':self.room})

    def post(self, request, slug):
        guest_form = GuestLoginForm(request.POST)
        user_form = UserLoginForm(request.POST)

        if guest_form.is_valid() and not user_form.is_valid():
            display_name = guest_form.cleaned_data['display_name']
            participant = Participant.objects.get_or_create(name=display_name, room=self.room, session=request.session)
            request.session['display_name'] = display_name
            request.session['participant_id'] = participant[0].id
            return render(request, self.conference_template_name, {"room":self.room, "participant":participant})
        
        elif user_form.is_valid():
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                participant = Participant.objects.get_or_create(name=username, user=user, room=self.room, session=request.session)
                return render(request, self.conference_template_name, {"room":self.room, "participant":participant})
            else:
                user_form.add_error(None, 'Invalid username or password')

        return render(request, self.template_name, {'guest_form': guest_form, 'user_form': user_form})
