from django.urls import path
from whiteboard.views import WhiteBoardView, ConferenceRoomMessagesAPI, SaveImageAPIView, Conference


urlpatterns = [
    path("", WhiteBoardView.as_view(), name="whiteboard"),

    path("confrence/<slug:slug>/", Conference.as_view(), name="confrence"),
    path('api/<slug:slug>/messages/', ConferenceRoomMessagesAPI.as_view()),
    path('api/<slug:slug>/save-image/', SaveImageAPIView.as_view()),
]
