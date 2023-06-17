from django.urls import path
from whiteboard.views import WhiteBoardView, ConferenceRoomMessagesAPI


urlpatterns = [
    path("", WhiteBoardView.as_view(), name="whiteboard"),


    path('<slug:slug>/messages/', ConferenceRoomMessagesAPI.as_view()),
]
