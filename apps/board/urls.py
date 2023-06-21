from django.urls import path
from board.views import SaveImageAPIView


urlpatterns = [
    path('api/<slug:slug>/save-image/', SaveImageAPIView.as_view()),
]
