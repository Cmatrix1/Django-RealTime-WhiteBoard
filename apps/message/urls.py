from django.urls import path
from message.views import ConferenceRoomMessagesAPI


urlpatterns = [
    path('api/<slug:slug>/messages/', ConferenceRoomMessagesAPI.as_view()),
]
