from django.urls import path
from whiteboard.views import WhiteBoardView, ConferenceRoomMessagesAPI, SaveImageAPIView


urlpatterns = [
    path("", WhiteBoardView.as_view(), name="whiteboard"),


    path('api/<slug:slug>/messages/', ConferenceRoomMessagesAPI.as_view()),
    path('api/<slug:slug>/save-image/', SaveImageAPIView.as_view()),
]
